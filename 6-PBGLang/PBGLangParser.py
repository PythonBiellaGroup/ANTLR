# Generated from PBGLang.g4 by ANTLR 4.10.1
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
        4,1,5,25,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,4,0,10,8,0,11,0,12,
        0,11,1,1,1,1,3,1,16,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,0,0,4,0,
        2,4,6,0,1,1,0,3,4,22,0,9,1,0,0,0,2,15,1,0,0,0,4,17,1,0,0,0,6,21,
        1,0,0,0,8,10,3,2,1,0,9,8,1,0,0,0,10,11,1,0,0,0,11,9,1,0,0,0,11,12,
        1,0,0,0,12,1,1,0,0,0,13,16,3,4,2,0,14,16,3,6,3,0,15,13,1,0,0,0,15,
        14,1,0,0,0,16,3,1,0,0,0,17,18,5,3,0,0,18,19,5,1,0,0,19,20,5,4,0,
        0,20,5,1,0,0,0,21,22,5,2,0,0,22,23,7,0,0,0,23,7,1,0,0,0,2,11,15
    ]

class PBGLangParser ( Parser ):

    grammarFileName = "PBGLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'mustra'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "VAR", "INT", 
                      "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_let = 2
    RULE_show = 3

    ruleNames =  [ "program", "statement", "let", "show" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    VAR=3
    INT=4
    WS=5

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PBGLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(PBGLangParser.StatementContext,i)


        def getRuleIndex(self):
            return PBGLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = PBGLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.statement()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==PBGLangParser.T__1 or _la==PBGLangParser.VAR):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def let(self):
            return self.getTypedRuleContext(PBGLangParser.LetContext,0)


        def show(self):
            return self.getTypedRuleContext(PBGLangParser.ShowContext,0)


        def getRuleIndex(self):
            return PBGLangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = PBGLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 15
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PBGLangParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.let()
                pass
            elif token in [PBGLangParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 14
                self.show()
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


    class LetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(PBGLangParser.VAR, 0)

        def INT(self):
            return self.getToken(PBGLangParser.INT, 0)

        def getRuleIndex(self):
            return PBGLangParser.RULE_let

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLet" ):
                listener.enterLet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLet" ):
                listener.exitLet(self)




    def let(self):

        localctx = PBGLangParser.LetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_let)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.match(PBGLangParser.VAR)
            self.state = 18
            self.match(PBGLangParser.T__0)
            self.state = 19
            self.match(PBGLangParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(PBGLangParser.INT, 0)

        def VAR(self):
            return self.getToken(PBGLangParser.VAR, 0)

        def getRuleIndex(self):
            return PBGLangParser.RULE_show

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShow" ):
                listener.enterShow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShow" ):
                listener.exitShow(self)




    def show(self):

        localctx = PBGLangParser.ShowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_show)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.match(PBGLangParser.T__1)
            self.state = 22
            _la = self._input.LA(1)
            if not(_la==PBGLangParser.VAR or _la==PBGLangParser.INT):
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





