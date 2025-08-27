# Generated from Part.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .Part import Part
else:
    from Part import Part

# This class defines a complete listener for a parse tree produced by Part.
class PartListener(ParseTreeListener):

    # Enter a parse tree produced by Part#part.
    def enterPart(self, ctx:Part.PartContext):
        pass

    # Exit a parse tree produced by Part#part.
    def exitPart(self, ctx:Part.PartContext):
        pass


    # Enter a parse tree produced by Part#partBody.
    def enterPartBody(self, ctx:Part.PartBodyContext):
        pass

    # Exit a parse tree produced by Part#partBody.
    def exitPartBody(self, ctx:Part.PartBodyContext):
        pass


    # Enter a parse tree produced by Part#expr.
    def enterExpr(self, ctx:Part.ExprContext):
        pass

    # Exit a parse tree produced by Part#expr.
    def exitExpr(self, ctx:Part.ExprContext):
        pass


    # Enter a parse tree produced by Part#unit.
    def enterUnit(self, ctx:Part.UnitContext):
        pass

    # Exit a parse tree produced by Part#unit.
    def exitUnit(self, ctx:Part.UnitContext):
        pass



del Part