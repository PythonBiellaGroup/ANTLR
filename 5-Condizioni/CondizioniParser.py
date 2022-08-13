# Generated from Condizioni.g by ANTLR 4.10.1
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
        4,1,7,39,2,0,7,0,2,1,7,1,2,2,7,2,1,0,4,0,8,8,0,11,0,12,0,9,1,0,1,
        0,1,1,1,1,1,1,1,1,1,1,3,1,19,8,1,1,1,1,1,3,1,23,8,1,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,5,2,34,8,2,10,2,12,2,37,9,2,1,2,0,1,4,3,
        0,2,4,0,0,40,0,7,1,0,0,0,2,22,1,0,0,0,4,24,1,0,0,0,6,8,3,2,1,0,7,
        6,1,0,0,0,8,9,1,0,0,0,9,7,1,0,0,0,9,10,1,0,0,0,10,11,1,0,0,0,11,
        12,5,0,0,1,12,1,1,0,0,0,13,14,5,1,0,0,14,15,3,4,2,0,15,18,3,2,1,
        0,16,17,5,2,0,0,17,19,3,2,1,0,18,16,1,0,0,0,18,19,1,0,0,0,19,23,
        1,0,0,0,20,21,5,3,0,0,21,23,3,4,2,0,22,13,1,0,0,0,22,20,1,0,0,0,
        23,3,1,0,0,0,24,25,6,2,-1,0,25,26,5,6,0,0,26,35,1,0,0,0,27,28,10,
        3,0,0,28,29,5,4,0,0,29,34,3,4,2,4,30,31,10,2,0,0,31,32,5,5,0,0,32,
        34,3,4,2,3,33,27,1,0,0,0,33,30,1,0,0,0,34,37,1,0,0,0,35,33,1,0,0,
        0,35,36,1,0,0,0,36,5,1,0,0,0,37,35,1,0,0,0,5,9,18,22,33,35
    ]

class CondizioniParser ( Parser ):

    grammarFileName = "Condizioni.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'print'", "'>'", "'<'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "GT", "LT", "NUM", "WS" ]

    RULE_root = 0
    RULE_action = 1
    RULE_expr = 2

    ruleNames =  [ "root", "action", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    GT=4
    LT=5
    NUM=6
    WS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CondizioniParser.EOF, 0)

        def action(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CondizioniParser.ActionContext)
            else:
                return self.getTypedRuleContext(CondizioniParser.ActionContext,i)


        def getRuleIndex(self):
            return CondizioniParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = CondizioniParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.action()
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CondizioniParser.T__0 or _la==CondizioniParser.T__2):
                    break

            self.state = 11
            self.match(CondizioniParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CondizioniParser.RULE_action

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ConditionContext(ActionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CondizioniParser.ActionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CondizioniParser.ExprContext,0)

        def action(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CondizioniParser.ActionContext)
            else:
                return self.getTypedRuleContext(CondizioniParser.ActionContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)


    class PrintContext(ActionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CondizioniParser.ActionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CondizioniParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)



    def action(self):

        localctx = CondizioniParser.ActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_action)
        try:
            self.state = 22
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CondizioniParser.T__0]:
                localctx = CondizioniParser.ConditionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.match(CondizioniParser.T__0)
                self.state = 14
                self.expr(0)
                self.state = 15
                self.action()
                self.state = 18
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 16
                    self.match(CondizioniParser.T__1)
                    self.state = 17
                    self.action()


                pass
            elif token in [CondizioniParser.T__2]:
                localctx = CondizioniParser.PrintContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.match(CondizioniParser.T__2)
                self.state = 21
                self.expr(0)
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


        def getRuleIndex(self):
            return CondizioniParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ValueContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CondizioniParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(CondizioniParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)


    class LtContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CondizioniParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CondizioniParser.ExprContext)
            else:
                return self.getTypedRuleContext(CondizioniParser.ExprContext,i)

        def LT(self):
            return self.getToken(CondizioniParser.LT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLt" ):
                return visitor.visitLt(self)
            else:
                return visitor.visitChildren(self)


    class GtContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CondizioniParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CondizioniParser.ExprContext)
            else:
                return self.getTypedRuleContext(CondizioniParser.ExprContext,i)

        def GT(self):
            return self.getToken(CondizioniParser.GT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGt" ):
                return visitor.visitGt(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CondizioniParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = CondizioniParser.ValueContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 25
            self.match(CondizioniParser.NUM)
            self._ctx.stop = self._input.LT(-1)
            self.state = 35
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 33
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = CondizioniParser.GtContext(self, CondizioniParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 27
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 28
                        self.match(CondizioniParser.GT)
                        self.state = 29
                        self.expr(4)
                        pass

                    elif la_ == 2:
                        localctx = CondizioniParser.LtContext(self, CondizioniParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 30
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 31
                        self.match(CondizioniParser.LT)
                        self.state = 32
                        self.expr(3)
                        pass

             
                self.state = 37
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




