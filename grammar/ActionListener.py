# Generated from Action.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .Action import Action
else:
    from Action import Action

# This class defines a complete listener for a parse tree produced by Action.
class ActionListener(ParseTreeListener):

    # Enter a parse tree produced by Action#action.
    def enterAction(self, ctx:Action.ActionContext):
        pass

    # Exit a parse tree produced by Action#action.
    def exitAction(self, ctx:Action.ActionContext):
        pass


    # Enter a parse tree produced by Action#param.
    def enterParam(self, ctx:Action.ParamContext):
        pass

    # Exit a parse tree produced by Action#param.
    def exitParam(self, ctx:Action.ParamContext):
        pass


    # Enter a parse tree produced by Action#attribute.
    def enterAttribute(self, ctx:Action.AttributeContext):
        pass

    # Exit a parse tree produced by Action#attribute.
    def exitAttribute(self, ctx:Action.AttributeContext):
        pass


    # Enter a parse tree produced by Action#attributeInit.
    def enterAttributeInit(self, ctx:Action.AttributeInitContext):
        pass

    # Exit a parse tree produced by Action#attributeInit.
    def exitAttributeInit(self, ctx:Action.AttributeInitContext):
        pass


    # Enter a parse tree produced by Action#flowStatement.
    def enterFlowStatement(self, ctx:Action.FlowStatementContext):
        pass

    # Exit a parse tree produced by Action#flowStatement.
    def exitFlowStatement(self, ctx:Action.FlowStatementContext):
        pass


    # Enter a parse tree produced by Action#firstStep.
    def enterFirstStep(self, ctx:Action.FirstStepContext):
        pass

    # Exit a parse tree produced by Action#firstStep.
    def exitFirstStep(self, ctx:Action.FirstStepContext):
        pass


    # Enter a parse tree produced by Action#thenStep.
    def enterThenStep(self, ctx:Action.ThenStepContext):
        pass

    # Exit a parse tree produced by Action#thenStep.
    def exitThenStep(self, ctx:Action.ThenStepContext):
        pass


    # Enter a parse tree produced by Action#ifStatement.
    def enterIfStatement(self, ctx:Action.IfStatementContext):
        pass

    # Exit a parse tree produced by Action#ifStatement.
    def exitIfStatement(self, ctx:Action.IfStatementContext):
        pass


    # Enter a parse tree produced by Action#flowBody.
    def enterFlowBody(self, ctx:Action.FlowBodyContext):
        pass

    # Exit a parse tree produced by Action#flowBody.
    def exitFlowBody(self, ctx:Action.FlowBodyContext):
        pass


    # Enter a parse tree produced by Action#condition.
    def enterCondition(self, ctx:Action.ConditionContext):
        pass

    # Exit a parse tree produced by Action#condition.
    def exitCondition(self, ctx:Action.ConditionContext):
        pass


    # Enter a parse tree produced by Action#comparison.
    def enterComparison(self, ctx:Action.ComparisonContext):
        pass

    # Exit a parse tree produced by Action#comparison.
    def exitComparison(self, ctx:Action.ComparisonContext):
        pass


    # Enter a parse tree produced by Action#compareOp.
    def enterCompareOp(self, ctx:Action.CompareOpContext):
        pass

    # Exit a parse tree produced by Action#compareOp.
    def exitCompareOp(self, ctx:Action.CompareOpContext):
        pass


    # Enter a parse tree produced by Action#expr.
    def enterExpr(self, ctx:Action.ExprContext):
        pass

    # Exit a parse tree produced by Action#expr.
    def exitExpr(self, ctx:Action.ExprContext):
        pass


    # Enter a parse tree produced by Action#part.
    def enterPart(self, ctx:Action.PartContext):
        pass

    # Exit a parse tree produced by Action#part.
    def exitPart(self, ctx:Action.PartContext):
        pass


    # Enter a parse tree produced by Action#partBody.
    def enterPartBody(self, ctx:Action.PartBodyContext):
        pass

    # Exit a parse tree produced by Action#partBody.
    def exitPartBody(self, ctx:Action.PartBodyContext):
        pass


    # Enter a parse tree produced by Action#unit.
    def enterUnit(self, ctx:Action.UnitContext):
        pass

    # Exit a parse tree produced by Action#unit.
    def exitUnit(self, ctx:Action.UnitContext):
        pass



del Action