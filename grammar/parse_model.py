from antlr4 import *
from .CommonLexer import CommonLexer
from .Model import Model as ModelParser
from .ModelVisitor import ModelVisitor
import json
from rich import print as rprint

class MXFVisitor(ModelVisitor):
    def __init__(self):
        super().__init__()
        self.package_name = None  # Package name if declared
        self.imports = []         # List of import statements
        self.actions = []         # top-level actions
        self.parts = []           # top-level parts
        self.nested_actions = {}  # map action_name -> action dict
        self.current_action = None
        self.current_flow = []

    def visitPackageDecl(self, ctx):
        """Visit package declaration: package QualifiedName { ... }"""
        self.package_name = self.visitQualifiedName(ctx.qualifiedName())
        
        # Visit imports and actions/parts inside the package
        for import_ctx in ctx.importDecl():
            self.visitImportDecl(import_ctx)
        
        for action_ctx in ctx.action():
            self.visitAction(action_ctx)  # visitAction adds to self.actions internally
        
        for part_ctx in ctx.part():
            self.parts.append(self.visitPart(part_ctx))
        
        return None
    
    def visitImportDecl(self, ctx):
        """Visit import declaration: private? import QualifiedName::*;"""
        is_private = ctx.PRIVATE() is not None
        qualified_name = self.visitQualifiedName(ctx.qualifiedName())
        
        import_info = {
            "private": is_private,
            "qualified_name": qualified_name,
            "wildcard": True  # Currently only supporting ::* imports
        }
        self.imports.append(import_info)
        return import_info
    
    def visitQualifiedName(self, ctx):
        """Visit qualified name: ID::ID::..."""
        if ctx is None:
            return None
        ids = [id_node.getText() for id_node in ctx.ID()]
        return "::".join(ids)

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
        elif ctx.ifStatement():
            return self.visitIfStatement(ctx.ifStatement())
        return None

    def visitIfStatement(self, ctx):
        """Visit if statement: if(condition) { perform action; } else { perform action; }"""
        # Parse condition
        condition_str = self.visitCondition(ctx.condition()) if ctx.condition() else None
        
        # Get all flowBody contexts
        all_flow_bodies = ctx.flowBody()
        
        # Determine how many belong to if vs else branch
        # Count braces to figure out the split
        has_else = ctx.ELSE() is not None
        
        if has_else:
            # Need to split flowBody between if and else blocks
            # This is tricky - we need to track which flows belong where
            # For now, simple approach: get LBRACE positions
            if_branch = []
            else_branch = []
            
            # Find the index where else starts by looking at the parse tree structure
            # A simpler approach: collect all, split in half (works for simple cases)
            mid = len(all_flow_bodies) // 2
            
            for i, flow_ctx in enumerate(all_flow_bodies):
                if flow_ctx.PERFORM():
                    action_name = flow_ctx.ID().getText()
                    action_obj = self.nested_actions.get(action_name, {"name": action_name})
                    if i < mid:
                        if_branch.append(action_obj)
                    else:
                        else_branch.append(action_obj)
        else:
            # No else clause, all flows belong to if
            if_branch = []
            for flow_ctx in all_flow_bodies:
                if flow_ctx.PERFORM():
                    action_name = flow_ctx.ID().getText()
                    action_obj = self.nested_actions.get(action_name, {"name": action_name})
                    if_branch.append(action_obj)
            else_branch = None
        
        # Create if statement object
        if_obj = {
            "type": "if",
            "condition": condition_str,
            "if_branch": if_branch,
            "else_branch": else_branch
        }
        
        self.current_flow.append(if_obj)
        return if_obj

    def visitCondition(self, ctx):
        """Visit condition and build string representation"""
        if ctx.AND():
            # Binary AND
            left = self.visitCondition(ctx.condition(0))
            right = self.visitCondition(ctx.condition(1))
            return f"{left} and {right}"
        elif ctx.OR():
            # Binary OR
            left = self.visitCondition(ctx.condition(0))
            right = self.visitCondition(ctx.condition(1))
            return f"{left} or {right}"
        elif ctx.NOT():
            # Unary NOT
            inner = self.visitCondition(ctx.condition(0))
            return f"not ({inner})"
        elif ctx.LPAREN() and ctx.RPAREN():
            # Parenthesized condition
            inner = self.visitCondition(ctx.condition(0))
            return f"({inner})"
        elif ctx.comparison():
            # Comparison expression
            return self.visitComparison(ctx.comparison())
        return "unknown"

    def visitComparison(self, ctx):
        """Visit comparison: expr op expr"""
        left = self.visitExpr(ctx.expr(0))
        right = self.visitExpr(ctx.expr(1))
        op = ctx.compareOp().getText()
        return f"{left} {op} {right}"

    def visitExpr(self, ctx):
        """Visit expression and return string representation"""
        if ctx.STRING():
            return ctx.STRING().getText()
        elif ctx.NUMBER():
            return ctx.NUMBER().getText()
        elif len(ctx.ID()) == 3:  # ID.ID.ID
            return f"{ctx.ID(0).getText()}.{ctx.ID(1).getText()}.{ctx.ID(2).getText()}"
        elif len(ctx.ID()) == 2:  # ID.ID
            return f"{ctx.ID(0).getText()}.{ctx.ID(1).getText()}"
        elif len(ctx.ID()) == 1:  # ID
            return ctx.ID(0).getText()
        return "unknown"

def parse_model(input_file, output_format='sysml'):
    """
    Parse a SysML model file
    
    Args:
        input_file: Path to the .sysml file
        output_format: 'sysml' (default) or 'uppaal'
    
    Returns:
        Dict with parsed model in requested format
    """
    input_stream = FileStream(input_file, encoding='utf-8')
    lexer = CommonLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ModelParser(stream)
    tree = parser.model()

    visitor = MXFVisitor()
    visitor.visit(tree)
    
    result = {
        "package": visitor.package_name,
        "imports": visitor.imports,
        "actions": visitor.actions,
        "parts": visitor.parts
    }
    
    if output_format == 'uppaal':
        # Import here to avoid circular dependency
        import sys
        import os
        sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from uppaal_transformer import transform_to_uppaal
        return transform_to_uppaal(result)
    
    return result

def main():
    input_file = "sample.sysml"  
    output_file = "sample.json"
    uppaal_output_file = "sample_uppaal.json"
    
    # Parse SysML format
    result_sysml = parse_model(input_file, output_format='sysml')

    rprint("[bold green]Parsed Model (SysML format):[/bold green]")
    rprint(f"Package: {result_sysml['package']}")
    rprint(f"Imports: {len(result_sysml['imports'])}")
    rprint(f"Actions: {len(result_sysml['actions'])}")

    # Save SysML format JSON
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(result_sysml, f, indent=2, ensure_ascii=False)
        rprint(f"[bold blue]SysML JSON saved to: {output_file}[/bold blue]")
    except IOError as e:
        rprint(f"[bold red]Error saving SysML JSON: {e}[/bold red]")
    
    # Generate UPPAAL format
    try:
        result_uppaal = parse_model(input_file, output_format='uppaal')
        
        rprint("\n[bold green]Generated UPPAAL Model:[/bold green]")
        rprint(f"Templates: {len(result_uppaal['model']['templates'])}")
        for template in result_uppaal['model']['templates']:
            rprint(f"  - {template['name']} ({template['type']}): {len(template['states'])} states, {len(template['transitions'])} transitions")
        rprint(f"Channels: {len(result_uppaal['model']['channels'])}")
        rprint(f"Global Variables: {len(result_uppaal['model']['global_declarations']['variables'])}")
        
        # Save UPPAAL format JSON
        with open(uppaal_output_file, 'w', encoding='utf-8') as f:
            json.dump(result_uppaal, f, indent=2, ensure_ascii=False)
        rprint(f"[bold blue]UPPAAL JSON saved to: {uppaal_output_file}[/bold blue]")
    except Exception as e:
        rprint(f"[bold red]Error generating UPPAAL JSON: {e}[/bold red]")
        import traceback
        traceback.print_exc()



if __name__ == '__main__':
    main()
