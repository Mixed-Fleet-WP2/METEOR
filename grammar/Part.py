# Generated from Part.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,22,43,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,0,1,0,1,
        0,5,0,15,8,0,10,0,12,0,18,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,3,
        1,28,8,1,1,1,1,1,1,1,1,1,1,1,3,1,35,8,1,1,2,1,2,1,3,1,3,1,3,1,3,
        1,3,0,0,4,0,2,4,6,0,1,1,0,19,21,41,0,8,1,0,0,0,2,34,1,0,0,0,4,36,
        1,0,0,0,6,38,1,0,0,0,8,9,5,2,0,0,9,10,5,19,0,0,10,11,5,11,0,0,11,
        12,5,19,0,0,12,16,5,15,0,0,13,15,3,2,1,0,14,13,1,0,0,0,15,18,1,0,
        0,0,16,14,1,0,0,0,16,17,1,0,0,0,17,19,1,0,0,0,18,16,1,0,0,0,19,20,
        5,16,0,0,20,1,1,0,0,0,21,22,5,6,0,0,22,23,5,7,0,0,23,24,5,19,0,0,
        24,25,5,13,0,0,25,27,3,4,2,0,26,28,3,6,3,0,27,26,1,0,0,0,27,28,1,
        0,0,0,28,29,1,0,0,0,29,30,5,12,0,0,30,35,1,0,0,0,31,32,5,5,0,0,32,
        33,5,19,0,0,33,35,5,12,0,0,34,21,1,0,0,0,34,31,1,0,0,0,35,3,1,0,
        0,0,36,37,7,0,0,0,37,5,1,0,0,0,38,39,5,17,0,0,39,40,5,19,0,0,40,
        41,5,18,0,0,41,7,1,0,0,0,3,16,27,34
    ]

class Part ( Parser ):

    grammarFileName = "Part.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'action'", "'part'", "'in'", "'out'", 
                     "'perform'", "'attribute'", "':>>'", "'first'", "'then'", 
                     "'done'", "':'", "';'", "'='", "'.'", "'{'", "'}'", 
                     "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "ACTION", "PART", "IN", "OUT", "PERFORM", 
                      "ATTRIBUTE", "REDEFINES", "FIRST", "THEN", "DONE", 
                      "COLON", "SEMI", "EQUAL", "DOT", "LBRACE", "RBRACE", 
                      "LBRACK", "RBRACK", "ID", "STRING", "NUMBER", "WS" ]

    RULE_part = 0
    RULE_partBody = 1
    RULE_expr = 2
    RULE_unit = 3

    ruleNames =  [ "part", "partBody", "expr", "unit" ]

    EOF = Token.EOF
    ACTION=1
    PART=2
    IN=3
    OUT=4
    PERFORM=5
    ATTRIBUTE=6
    REDEFINES=7
    FIRST=8
    THEN=9
    DONE=10
    COLON=11
    SEMI=12
    EQUAL=13
    DOT=14
    LBRACE=15
    RBRACE=16
    LBRACK=17
    RBRACK=18
    ID=19
    STRING=20
    NUMBER=21
    WS=22

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class PartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PART(self):
            return self.getToken(Part.PART, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(Part.ID)
            else:
                return self.getToken(Part.ID, i)

        def COLON(self):
            return self.getToken(Part.COLON, 0)

        def LBRACE(self):
            return self.getToken(Part.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(Part.RBRACE, 0)

        def partBody(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Part.PartBodyContext)
            else:
                return self.getTypedRuleContext(Part.PartBodyContext,i)


        def getRuleIndex(self):
            return Part.RULE_part

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPart" ):
                listener.enterPart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPart" ):
                listener.exitPart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPart" ):
                return visitor.visitPart(self)
            else:
                return visitor.visitChildren(self)




    def part(self):

        localctx = Part.PartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.match(Part.PART)
            self.state = 9
            self.match(Part.ID)
            self.state = 10
            self.match(Part.COLON)
            self.state = 11
            self.match(Part.ID)
            self.state = 12
            self.match(Part.LBRACE)
            self.state = 16
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5 or _la==6:
                self.state = 13
                self.partBody()
                self.state = 18
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 19
            self.match(Part.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PartBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ATTRIBUTE(self):
            return self.getToken(Part.ATTRIBUTE, 0)

        def REDEFINES(self):
            return self.getToken(Part.REDEFINES, 0)

        def ID(self):
            return self.getToken(Part.ID, 0)

        def EQUAL(self):
            return self.getToken(Part.EQUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(Part.ExprContext,0)


        def SEMI(self):
            return self.getToken(Part.SEMI, 0)

        def unit(self):
            return self.getTypedRuleContext(Part.UnitContext,0)


        def PERFORM(self):
            return self.getToken(Part.PERFORM, 0)

        def getRuleIndex(self):
            return Part.RULE_partBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPartBody" ):
                listener.enterPartBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPartBody" ):
                listener.exitPartBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPartBody" ):
                return visitor.visitPartBody(self)
            else:
                return visitor.visitChildren(self)




    def partBody(self):

        localctx = Part.PartBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_partBody)
        self._la = 0 # Token type
        try:
            self.state = 34
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.match(Part.ATTRIBUTE)
                self.state = 22
                self.match(Part.REDEFINES)
                self.state = 23
                self.match(Part.ID)
                self.state = 24
                self.match(Part.EQUAL)
                self.state = 25
                self.expr()
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==17:
                    self.state = 26
                    self.unit()


                self.state = 29
                self.match(Part.SEMI)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.match(Part.PERFORM)
                self.state = 32
                self.match(Part.ID)
                self.state = 33
                self.match(Part.SEMI)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(Part.ID, 0)

        def STRING(self):
            return self.getToken(Part.STRING, 0)

        def NUMBER(self):
            return self.getToken(Part.NUMBER, 0)

        def getRuleIndex(self):
            return Part.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = Part.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3670016) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(Part.LBRACK, 0)

        def ID(self):
            return self.getToken(Part.ID, 0)

        def RBRACK(self):
            return self.getToken(Part.RBRACK, 0)

        def getRuleIndex(self):
            return Part.RULE_unit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnit" ):
                listener.enterUnit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnit" ):
                listener.exitUnit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnit" ):
                return visitor.visitUnit(self)
            else:
                return visitor.visitChildren(self)




    def unit(self):

        localctx = Part.UnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_unit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(Part.LBRACK)
            self.state = 39
            self.match(Part.ID)
            self.state = 40
            self.match(Part.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





