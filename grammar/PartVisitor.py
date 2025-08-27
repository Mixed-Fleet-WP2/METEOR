# Generated from Part.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .Part import Part
else:
    from Part import Part

# This class defines a complete generic visitor for a parse tree produced by Part.

class PartVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by Part#part.
    def visitPart(self, ctx:Part.PartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Part#partBody.
    def visitPartBody(self, ctx:Part.PartBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Part#expr.
    def visitExpr(self, ctx:Part.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Part#unit.
    def visitUnit(self, ctx:Part.UnitContext):
        return self.visitChildren(ctx)



del Part