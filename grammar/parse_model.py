from antlr4 import *
from .CommonLexer import CommonLexer
from .Model import Model as ModelParser
from .ModelVisitor import ModelVisitor
import json
from rich import print as rprint

class MXFVisitor(ModelVisitor):
    def __init__(self):
        super().__init__()
        self.actions = []       # top-level actions
        self.parts = []         # top-level parts
        self.nested_actions = {}  # map action_name -> action dict
        self.current_action = None
        self.current_flow = []

    def visitAction(self, ctx):
        action_name = ctx.ID(0).getText()
        action_type = ctx.ID(1).getText() if ctx.COLON() else None
        params = []
        parts = []
        nested_actions = []
        flow = []
        attributes = []
        for attr_ctx in ctx.attribute():
            attr_name = attr_ctx.ID(0).getText()
            attr_type = attr_ctx.ID(1).getText()
            fields = {}
            # Structured attribute with fields
            if attr_ctx.LBRACE():
                for init_ctx in attr_ctx.attributeInit():
                    field_name = init_ctx.ID().getText()
                    expr_ctx = init_ctx.expr()
                    if expr_ctx.NUMBER():
                        field_value = float(expr_ctx.NUMBER().getText())
                    elif expr_ctx.STRING():
                        field_value = expr_ctx.STRING().getText().strip('"')
                    else:
                        field_value = expr_ctx.getText()
                    fields[field_name] = field_value
                attributes.append({
                    "name": attr_name,
                    "type": attr_type,
                    "fields": fields
                })
            else:
                # Simple attribute (no nested fields)
                expr_ctx = attr_ctx.expr()
                if expr_ctx:
                    if expr_ctx.NUMBER():
                        value = float(expr_ctx.NUMBER().getText())
                    elif expr_ctx.STRING():
                        value = expr_ctx.STRING().getText().strip('"')
                    else:
                        value = expr_ctx.getText()
                    attributes.append({
                        "name": attr_name,
                        "type": attr_type,
                        "value": value
                    })
                else:
                    attributes.append({
                        "name": attr_name,
                        "type": attr_type
                    })


        # Save current action context to fill nested inside
        prev_action = self.current_action
        prev_flow = self.current_flow
        self.current_action = action_name
        self.current_flow = []

        # Parse params, parts, nested actions and flow statements
        for child in ctx.getChildren():
            rule_name = type(child).__name__
            # param() children
            if hasattr(child, 'getRuleIndex'):
                idx = child.getRuleIndex()
                # visit param, part, action, flowStatement by rule index
                # But better to explicitly call visit on children
            # We just visit children to fill self.current_flow and nested_actions
            self.visit(child)

        # After visiting children, self.current_flow has flow info
        flow = self.current_flow

        # Collect parts defined inside this action
        for part_ctx in ctx.part():
            parts.append(self.visitPart(part_ctx))

        # Collect nested actions inside this action (excluding self)
        for action_ctx in ctx.action():
            # Avoid including self recursively
            if action_ctx == ctx:
                continue
            nested_action = self.visitAction(action_ctx)
            nested_actions.append(nested_action)
            # Also save to map for flow lookup
            self.nested_actions[nested_action['name']] = nested_action

        # Compose current action dict
        action_dict = {
        "name": action_name,
        "type": action_type,
        "attributes": attributes if attributes else None,
        "params": params,
        "parts": parts if parts else None,
        "nested_actions": nested_actions if nested_actions else None,
        "flow": flow if flow else None,
    }

        # Fill params properly by visiting param children
        params = []
        for param_ctx in ctx.param():
            direction = param_ctx.getChild(0).getText()
            if direction == 'in':
                param_name = param_ctx.ID().getText()
                expr_ctx = param_ctx.expr()

                # Determine type of expr
                if expr_ctx:
                    if expr_ctx.NUMBER():
                        default_value = {"type": "number", "value": float(expr_ctx.NUMBER().getText())}
                    elif expr_ctx.STRING():
                        default_value = {"type": "string", "value": expr_ctx.STRING().getText().strip('"')}
                    elif expr_ctx.ID() and len(expr_ctx.ID()) == 1:
                        default_value = {"type": "attribute_ref", "value": expr_ctx.ID(0).getText()}
                    elif expr_ctx.ID() and len(expr_ctx.ID()) == 2 and expr_ctx.DOT():
                        default_value = {
                            "type": "qualified_id",
                            "value": f"{expr_ctx.ID(0).getText()}.{expr_ctx.ID(1).getText()}"
                        }
                    else:
                        default_value = {"type": "unknown", "value": expr_ctx.getText()}
                else:
                    default_value = None

                redefines_token = param_ctx.REDEFINES()
                has_redefines = redefines_token is not None
                params.append({
                    "direction": direction,
                    "name": param_name,
                    "default": default_value,
                    "redefines": has_redefines,
                })
            else:
                param_name = param_ctx.ID().getText()
                params.append({
                    "direction": direction,
                    "name": param_name,
                    "default": None,
                    "redefines": False,
                })

        action_dict["params"] = params

        # Restore previous action context
        self.current_action = prev_action
        self.current_flow = prev_flow

        # If this is top-level (no parent action), append to self.actions
        if self.current_action is None:
            self.actions.append(action_dict)

        return action_dict

    def visitPart(self, ctx):
        part_name = ctx.ID(0).getText()
        part_type = ctx.ID(1).getText()
        attributes = []
        performs = []

        for body_ctx in ctx.partBody():
            if body_ctx.ATTRIBUTE():
                attr_name = body_ctx.ID().getText()
                attr_value = body_ctx.expr().getText() if body_ctx.expr() else None
                attributes.append({
                    "name": attr_name,
                    "value": attr_value,
                })
            elif body_ctx.PERFORM():
                performs.append(body_ctx.ID().getText())

        part_info = {
            "name": part_name,
            "type": part_type,
            "attributes": attributes,
            "performs": performs,
        }
        return part_info

    def visitFlowStatement(self, ctx):
        # firstStep: ignore in flow
        # thenStep: capture perform steps as full action objects, skip 'done'
        if ctx.firstStep():
            # first step example: "first start;"
            # we do not store it
            return None
        elif ctx.thenStep():
            then_ctx = ctx.thenStep()
            if then_ctx.DONE():
                # done step - end of flow, ignore
                return None
            elif then_ctx.PERFORM():
                action_name = then_ctx.ID().getText()
                # Lookup full nested action if exists, else just name
                action_obj = self.nested_actions.get(action_name, {"name": action_name})
                self.current_flow.append(action_obj)
                return action_obj
        return None

def parse_model(input_file):
    input_stream = FileStream(input_file, encoding='utf-8')
    lexer = CommonLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ModelParser(stream)
    tree = parser.model()

    visitor = MXFVisitor()
    visitor.visit(tree)
    return visitor.actions

def main():
    input_file = "sample.mxf"  
    output_file = "sample.json"  
    input_stream = FileStream(input_file, encoding='utf-8')

    lexer = CommonLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ModelParser(stream)
    tree = parser.model()

    visitor = MXFVisitor()
    visitor.visit(tree)

    rprint("[bold green]Parsed Actions (with nested flow objects):[/bold green]")
    #rprint(json.dumps(visitor.actions, indent=2))

    # Save to JSON file
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(visitor.actions, f, indent=2, ensure_ascii=False)
        rprint(f"[bold blue]JSON output saved to: {output_file}[/bold blue]")
    except IOError as e:
        rprint(f"[bold red]Error saving JSON file: {e}[/bold red]")



if __name__ == '__main__':
    main()
