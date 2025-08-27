# Generated from Action.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .Action import Action
else:
    from Action import Action

# This class defines a complete generic visitor for a parse tree produced by Action.

class ActionVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by Action#action.
    def visitAction(self, ctx:Action.ActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Action#param.
    def visitParam(self, ctx:Action.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Action#attribute.
    def visitAttribute(self, ctx:Action.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Action#attributeInit.
    def visitAttributeInit(self, ctx:Action.AttributeInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Action#flowStatement.
    def visitFlowStatement(self, ctx:Action.FlowStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Action#firstStep.
    def visitFirstStep(self, ctx:Action.FirstStepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Action#thenStep.
    def visitThenStep(self, ctx:Action.ThenStepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Action#expr.
    def visitExpr(self, ctx:Action.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Action#part.
    def visitPart(self, ctx:Action.PartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Action#partBody.
    def visitPartBody(self, ctx:Action.PartBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Action#unit.
    def visitUnit(self, ctx:Action.UnitContext):
        return self.visitChildren(ctx)



del Action