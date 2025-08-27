# Generated from Model.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .Model import Model
else:
    from Model import Model

# This class defines a complete generic visitor for a parse tree produced by Model.

class ModelVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by Model#model.
    def visitModel(self, ctx:Model.ModelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Model#action.
    def visitAction(self, ctx:Model.ActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Model#param.
    def visitParam(self, ctx:Model.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Model#attribute.
    def visitAttribute(self, ctx:Model.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Model#attributeInit.
    def visitAttributeInit(self, ctx:Model.AttributeInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Model#flowStatement.
    def visitFlowStatement(self, ctx:Model.FlowStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Model#firstStep.
    def visitFirstStep(self, ctx:Model.FirstStepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Model#thenStep.
    def visitThenStep(self, ctx:Model.ThenStepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Model#expr.
    def visitExpr(self, ctx:Model.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Model#part.
    def visitPart(self, ctx:Model.PartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Model#partBody.
    def visitPartBody(self, ctx:Model.PartBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Model#unit.
    def visitUnit(self, ctx:Model.UnitContext):
        return self.visitChildren(ctx)



del Model