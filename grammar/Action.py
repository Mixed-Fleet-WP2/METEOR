# Generated from Action.g4 by ANTLR 4.13.1
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
        4,1,22,135,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,0,1,0,3,0,27,8,0,1,
        0,1,0,1,0,1,0,1,0,1,0,5,0,35,8,0,10,0,12,0,38,9,0,1,0,1,0,1,1,1,
        1,3,1,44,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,54,8,1,1,2,1,2,
        1,2,1,2,1,2,1,2,5,2,62,8,2,10,2,12,2,65,9,2,1,2,3,2,68,8,2,1,2,1,
        2,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,3,4,80,8,4,1,5,1,5,1,5,1,5,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,3,6,93,8,6,1,7,1,7,1,7,1,7,1,7,1,7,3,7,101,
        8,7,1,8,1,8,1,8,1,8,1,8,1,8,5,8,109,8,8,10,8,12,8,112,9,8,1,8,1,
        8,1,9,1,9,1,9,1,9,1,9,1,9,3,9,122,8,9,1,9,1,9,1,9,1,9,1,9,3,9,129,
        8,9,1,10,1,10,1,10,1,10,1,10,0,0,11,0,2,4,6,8,10,12,14,16,18,20,
        0,0,141,0,22,1,0,0,0,2,53,1,0,0,0,4,55,1,0,0,0,6,71,1,0,0,0,8,79,
        1,0,0,0,10,81,1,0,0,0,12,92,1,0,0,0,14,100,1,0,0,0,16,102,1,0,0,
        0,18,128,1,0,0,0,20,130,1,0,0,0,22,23,5,1,0,0,23,26,5,19,0,0,24,
        25,5,11,0,0,25,27,5,19,0,0,26,24,1,0,0,0,26,27,1,0,0,0,27,28,1,0,
        0,0,28,36,5,15,0,0,29,35,3,4,2,0,30,35,3,16,8,0,31,35,3,2,1,0,32,
        35,3,8,4,0,33,35,3,0,0,0,34,29,1,0,0,0,34,30,1,0,0,0,34,31,1,0,0,
        0,34,32,1,0,0,0,34,33,1,0,0,0,35,38,1,0,0,0,36,34,1,0,0,0,36,37,
        1,0,0,0,37,39,1,0,0,0,38,36,1,0,0,0,39,40,5,16,0,0,40,1,1,0,0,0,
        41,43,5,3,0,0,42,44,5,7,0,0,43,42,1,0,0,0,43,44,1,0,0,0,44,45,1,
        0,0,0,45,46,5,19,0,0,46,47,5,13,0,0,47,48,3,14,7,0,48,49,5,12,0,
        0,49,54,1,0,0,0,50,51,5,4,0,0,51,52,5,19,0,0,52,54,5,12,0,0,53,41,
        1,0,0,0,53,50,1,0,0,0,54,3,1,0,0,0,55,56,5,6,0,0,56,57,5,19,0,0,
        57,58,5,11,0,0,58,67,5,19,0,0,59,63,5,15,0,0,60,62,3,6,3,0,61,60,
        1,0,0,0,62,65,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,66,1,0,0,0,
        65,63,1,0,0,0,66,68,5,16,0,0,67,59,1,0,0,0,67,68,1,0,0,0,68,69,1,
        0,0,0,69,70,5,12,0,0,70,5,1,0,0,0,71,72,5,7,0,0,72,73,5,19,0,0,73,
        74,5,13,0,0,74,75,3,14,7,0,75,76,5,12,0,0,76,7,1,0,0,0,77,80,3,10,
        5,0,78,80,3,12,6,0,79,77,1,0,0,0,79,78,1,0,0,0,80,9,1,0,0,0,81,82,
        5,8,0,0,82,83,5,19,0,0,83,84,5,12,0,0,84,11,1,0,0,0,85,86,5,9,0,
        0,86,87,5,10,0,0,87,93,5,12,0,0,88,89,5,9,0,0,89,90,5,5,0,0,90,91,
        5,19,0,0,91,93,5,12,0,0,92,85,1,0,0,0,92,88,1,0,0,0,93,13,1,0,0,
        0,94,101,5,19,0,0,95,96,5,19,0,0,96,97,5,14,0,0,97,101,5,19,0,0,
        98,101,5,20,0,0,99,101,5,21,0,0,100,94,1,0,0,0,100,95,1,0,0,0,100,
        98,1,0,0,0,100,99,1,0,0,0,101,15,1,0,0,0,102,103,5,2,0,0,103,104,
        5,19,0,0,104,105,5,11,0,0,105,106,5,19,0,0,106,110,5,15,0,0,107,
        109,3,18,9,0,108,107,1,0,0,0,109,112,1,0,0,0,110,108,1,0,0,0,110,
        111,1,0,0,0,111,113,1,0,0,0,112,110,1,0,0,0,113,114,5,16,0,0,114,
        17,1,0,0,0,115,116,5,6,0,0,116,117,5,7,0,0,117,118,5,19,0,0,118,
        119,5,13,0,0,119,121,3,14,7,0,120,122,3,20,10,0,121,120,1,0,0,0,
        121,122,1,0,0,0,122,123,1,0,0,0,123,124,5,12,0,0,124,129,1,0,0,0,
        125,126,5,5,0,0,126,127,5,19,0,0,127,129,5,12,0,0,128,115,1,0,0,
        0,128,125,1,0,0,0,129,19,1,0,0,0,130,131,5,17,0,0,131,132,5,19,0,
        0,132,133,5,18,0,0,133,21,1,0,0,0,13,26,34,36,43,53,63,67,79,92,
        100,110,121,128
    ]

class Action ( Parser ):

    grammarFileName = "Action.g4"

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

    RULE_action = 0
    RULE_param = 1
    RULE_attribute = 2
    RULE_attributeInit = 3
    RULE_flowStatement = 4
    RULE_firstStep = 5
    RULE_thenStep = 6
    RULE_expr = 7
    RULE_part = 8
    RULE_partBody = 9
    RULE_unit = 10

    ruleNames =  [ "action", "param", "attribute", "attributeInit", "flowStatement", 
                   "firstStep", "thenStep", "expr", "part", "partBody", 
                   "unit" ]

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




    class ActionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ACTION(self):
            return self.getToken(Action.ACTION, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(Action.ID)
            else:
                return self.getToken(Action.ID, i)

        def LBRACE(self):
            return self.getToken(Action.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(Action.RBRACE, 0)

        def COLON(self):
            return self.getToken(Action.COLON, 0)

        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Action.AttributeContext)
            else:
                return self.getTypedRuleContext(Action.AttributeContext,i)


        def part(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Action.PartContext)
            else:
                return self.getTypedRuleContext(Action.PartContext,i)


        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Action.ParamContext)
            else:
                return self.getTypedRuleContext(Action.ParamContext,i)


        def flowStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Action.FlowStatementContext)
            else:
                return self.getTypedRuleContext(Action.FlowStatementContext,i)


        def action(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Action.ActionContext)
            else:
                return self.getTypedRuleContext(Action.ActionContext,i)


        def getRuleIndex(self):
            return Action.RULE_action

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAction" ):
                listener.enterAction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAction" ):
                listener.exitAction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAction" ):
                return visitor.visitAction(self)
            else:
                return visitor.visitChildren(self)




    def action(self):

        localctx = Action.ActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_action)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(Action.ACTION)
            self.state = 23
            self.match(Action.ID)
            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 24
                self.match(Action.COLON)
                self.state = 25
                self.match(Action.ID)


            self.state = 28
            self.match(Action.LBRACE)
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 862) != 0):
                self.state = 34
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [6]:
                    self.state = 29
                    self.attribute()
                    pass
                elif token in [2]:
                    self.state = 30
                    self.part()
                    pass
                elif token in [3, 4]:
                    self.state = 31
                    self.param()
                    pass
                elif token in [8, 9]:
                    self.state = 32
                    self.flowStatement()
                    pass
                elif token in [1]:
                    self.state = 33
                    self.action()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 39
            self.match(Action.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IN(self):
            return self.getToken(Action.IN, 0)

        def ID(self):
            return self.getToken(Action.ID, 0)

        def EQUAL(self):
            return self.getToken(Action.EQUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(Action.ExprContext,0)


        def SEMI(self):
            return self.getToken(Action.SEMI, 0)

        def REDEFINES(self):
            return self.getToken(Action.REDEFINES, 0)

        def OUT(self):
            return self.getToken(Action.OUT, 0)

        def getRuleIndex(self):
            return Action.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = Action.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_param)
        self._la = 0 # Token type
        try:
            self.state = 53
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.match(Action.IN)
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==7:
                    self.state = 42
                    self.match(Action.REDEFINES)


                self.state = 45
                self.match(Action.ID)
                self.state = 46
                self.match(Action.EQUAL)
                self.state = 47
                self.expr()
                self.state = 48
                self.match(Action.SEMI)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.match(Action.OUT)
                self.state = 51
                self.match(Action.ID)
                self.state = 52
                self.match(Action.SEMI)
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


    class AttributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ATTRIBUTE(self):
            return self.getToken(Action.ATTRIBUTE, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(Action.ID)
            else:
                return self.getToken(Action.ID, i)

        def COLON(self):
            return self.getToken(Action.COLON, 0)

        def SEMI(self):
            return self.getToken(Action.SEMI, 0)

        def LBRACE(self):
            return self.getToken(Action.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(Action.RBRACE, 0)

        def attributeInit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Action.AttributeInitContext)
            else:
                return self.getTypedRuleContext(Action.AttributeInitContext,i)


        def getRuleIndex(self):
            return Action.RULE_attribute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute" ):
                listener.enterAttribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute" ):
                listener.exitAttribute(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute" ):
                return visitor.visitAttribute(self)
            else:
                return visitor.visitChildren(self)




    def attribute(self):

        localctx = Action.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_attribute)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(Action.ATTRIBUTE)
            self.state = 56
            self.match(Action.ID)
            self.state = 57
            self.match(Action.COLON)
            self.state = 58
            self.match(Action.ID)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 59
                self.match(Action.LBRACE)
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==7:
                    self.state = 60
                    self.attributeInit()
                    self.state = 65
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 66
                self.match(Action.RBRACE)


            self.state = 69
            self.match(Action.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REDEFINES(self):
            return self.getToken(Action.REDEFINES, 0)

        def ID(self):
            return self.getToken(Action.ID, 0)

        def EQUAL(self):
            return self.getToken(Action.EQUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(Action.ExprContext,0)


        def SEMI(self):
            return self.getToken(Action.SEMI, 0)

        def getRuleIndex(self):
            return Action.RULE_attributeInit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttributeInit" ):
                listener.enterAttributeInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttributeInit" ):
                listener.exitAttributeInit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributeInit" ):
                return visitor.visitAttributeInit(self)
            else:
                return visitor.visitChildren(self)




    def attributeInit(self):

        localctx = Action.AttributeInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_attributeInit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(Action.REDEFINES)
            self.state = 72
            self.match(Action.ID)
            self.state = 73
            self.match(Action.EQUAL)
            self.state = 74
            self.expr()
            self.state = 75
            self.match(Action.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FlowStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def firstStep(self):
            return self.getTypedRuleContext(Action.FirstStepContext,0)


        def thenStep(self):
            return self.getTypedRuleContext(Action.ThenStepContext,0)


        def getRuleIndex(self):
            return Action.RULE_flowStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFlowStatement" ):
                listener.enterFlowStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFlowStatement" ):
                listener.exitFlowStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFlowStatement" ):
                return visitor.visitFlowStatement(self)
            else:
                return visitor.visitChildren(self)




    def flowStatement(self):

        localctx = Action.FlowStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_flowStatement)
        try:
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.firstStep()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                self.thenStep()
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


    class FirstStepContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FIRST(self):
            return self.getToken(Action.FIRST, 0)

        def ID(self):
            return self.getToken(Action.ID, 0)

        def SEMI(self):
            return self.getToken(Action.SEMI, 0)

        def getRuleIndex(self):
            return Action.RULE_firstStep

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFirstStep" ):
                listener.enterFirstStep(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFirstStep" ):
                listener.exitFirstStep(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFirstStep" ):
                return visitor.visitFirstStep(self)
            else:
                return visitor.visitChildren(self)




    def firstStep(self):

        localctx = Action.FirstStepContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_firstStep)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(Action.FIRST)
            self.state = 82
            self.match(Action.ID)
            self.state = 83
            self.match(Action.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ThenStepContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def THEN(self):
            return self.getToken(Action.THEN, 0)

        def DONE(self):
            return self.getToken(Action.DONE, 0)

        def SEMI(self):
            return self.getToken(Action.SEMI, 0)

        def PERFORM(self):
            return self.getToken(Action.PERFORM, 0)

        def ID(self):
            return self.getToken(Action.ID, 0)

        def getRuleIndex(self):
            return Action.RULE_thenStep

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThenStep" ):
                listener.enterThenStep(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThenStep" ):
                listener.exitThenStep(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThenStep" ):
                return visitor.visitThenStep(self)
            else:
                return visitor.visitChildren(self)




    def thenStep(self):

        localctx = Action.ThenStepContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_thenStep)
        try:
            self.state = 92
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.match(Action.THEN)
                self.state = 86
                self.match(Action.DONE)
                self.state = 87
                self.match(Action.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 88
                self.match(Action.THEN)
                self.state = 89
                self.match(Action.PERFORM)
                self.state = 90
                self.match(Action.ID)
                self.state = 91
                self.match(Action.SEMI)
                pass


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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(Action.ID)
            else:
                return self.getToken(Action.ID, i)

        def DOT(self):
            return self.getToken(Action.DOT, 0)

        def STRING(self):
            return self.getToken(Action.STRING, 0)

        def NUMBER(self):
            return self.getToken(Action.NUMBER, 0)

        def getRuleIndex(self):
            return Action.RULE_expr

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

        localctx = Action.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_expr)
        try:
            self.state = 100
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                self.match(Action.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self.match(Action.ID)
                self.state = 96
                self.match(Action.DOT)
                self.state = 97
                self.match(Action.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 98
                self.match(Action.STRING)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 99
                self.match(Action.NUMBER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PART(self):
            return self.getToken(Action.PART, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(Action.ID)
            else:
                return self.getToken(Action.ID, i)

        def COLON(self):
            return self.getToken(Action.COLON, 0)

        def LBRACE(self):
            return self.getToken(Action.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(Action.RBRACE, 0)

        def partBody(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Action.PartBodyContext)
            else:
                return self.getTypedRuleContext(Action.PartBodyContext,i)


        def getRuleIndex(self):
            return Action.RULE_part

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

        localctx = Action.PartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(Action.PART)
            self.state = 103
            self.match(Action.ID)
            self.state = 104
            self.match(Action.COLON)
            self.state = 105
            self.match(Action.ID)
            self.state = 106
            self.match(Action.LBRACE)
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5 or _la==6:
                self.state = 107
                self.partBody()
                self.state = 112
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 113
            self.match(Action.RBRACE)
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
            return self.getToken(Action.ATTRIBUTE, 0)

        def REDEFINES(self):
            return self.getToken(Action.REDEFINES, 0)

        def ID(self):
            return self.getToken(Action.ID, 0)

        def EQUAL(self):
            return self.getToken(Action.EQUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(Action.ExprContext,0)


        def SEMI(self):
            return self.getToken(Action.SEMI, 0)

        def unit(self):
            return self.getTypedRuleContext(Action.UnitContext,0)


        def PERFORM(self):
            return self.getToken(Action.PERFORM, 0)

        def getRuleIndex(self):
            return Action.RULE_partBody

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

        localctx = Action.PartBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_partBody)
        self._la = 0 # Token type
        try:
            self.state = 128
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 115
                self.match(Action.ATTRIBUTE)
                self.state = 116
                self.match(Action.REDEFINES)
                self.state = 117
                self.match(Action.ID)
                self.state = 118
                self.match(Action.EQUAL)
                self.state = 119
                self.expr()
                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==17:
                    self.state = 120
                    self.unit()


                self.state = 123
                self.match(Action.SEMI)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.match(Action.PERFORM)
                self.state = 126
                self.match(Action.ID)
                self.state = 127
                self.match(Action.SEMI)
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


    class UnitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(Action.LBRACK, 0)

        def ID(self):
            return self.getToken(Action.ID, 0)

        def RBRACK(self):
            return self.getToken(Action.RBRACK, 0)

        def getRuleIndex(self):
            return Action.RULE_unit

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

        localctx = Action.UnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_unit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(Action.LBRACK)
            self.state = 131
            self.match(Action.ID)
            self.state = 132
            self.match(Action.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





