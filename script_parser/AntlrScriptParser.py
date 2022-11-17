# Generated from AntlrScriptParser.g4 by ANTLR 4.11.1
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
        4,1,14,23,2,0,7,0,2,1,7,1,2,2,7,2,1,0,5,0,8,8,0,10,0,12,0,11,9,0,
        1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,3,2,21,8,2,1,2,0,0,3,0,2,4,0,0,23,
        0,9,1,0,0,0,2,14,1,0,0,0,4,20,1,0,0,0,6,8,5,14,0,0,7,6,1,0,0,0,8,
        11,1,0,0,0,9,7,1,0,0,0,9,10,1,0,0,0,10,12,1,0,0,0,11,9,1,0,0,0,12,
        13,5,0,0,1,13,1,1,0,0,0,14,15,1,0,0,0,15,3,1,0,0,0,16,21,5,1,0,0,
        17,21,5,2,0,0,18,21,5,3,0,0,19,21,5,12,0,0,20,16,1,0,0,0,20,17,1,
        0,0,0,20,18,1,0,0,0,20,19,1,0,0,0,21,5,1,0,0,0,2,9,20
    ]

class AntlrScriptParser ( Parser ):

    grammarFileName = "AntlrScriptParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'integer'", "'boolean'", "'string'", 
                     "'entity'", "'module'", "':'", "';'", "'['", "']'", 
                     "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "INTEGER", "BOOLEAN", "STRING", "ENTITY", 
                      "MODULE", "COLON", "SEMI", "LSQRD", "RSQRD", "LCRLY", 
                      "RCRLY", "ID", "WS", "STATEMENT" ]

    RULE_script = 0
    RULE_statement = 1
    RULE_type_spec = 2

    ruleNames =  [ "script", "statement", "type_spec" ]

    EOF = Token.EOF
    INTEGER=1
    BOOLEAN=2
    STRING=3
    ENTITY=4
    MODULE=5
    COLON=6
    SEMI=7
    LSQRD=8
    RSQRD=9
    LCRLY=10
    RCRLY=11
    ID=12
    WS=13
    STATEMENT=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ScriptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(AntlrScriptParser.EOF, 0)

        def STATEMENT(self, i:int=None):
            if i is None:
                return self.getTokens(AntlrScriptParser.STATEMENT)
            else:
                return self.getToken(AntlrScriptParser.STATEMENT, i)

        def getRuleIndex(self):
            return AntlrScriptParser.RULE_script

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScript" ):
                listener.enterScript(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScript" ):
                listener.exitScript(self)




    def script(self):

        localctx = AntlrScriptParser.ScriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_script)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 6
                self.match(AntlrScriptParser.STATEMENT)
                self.state = 11
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 12
            self.match(AntlrScriptParser.EOF)
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


        def getRuleIndex(self):
            return AntlrScriptParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = AntlrScriptParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_specContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AntlrScriptParser.RULE_type_spec

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class String_typeContext(Type_specContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AntlrScriptParser.Type_specContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(AntlrScriptParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString_type" ):
                listener.enterString_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString_type" ):
                listener.exitString_type(self)


    class Entity_typeContext(Type_specContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AntlrScriptParser.Type_specContext
            super().__init__(parser)
            self.target = None # Token
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(AntlrScriptParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntity_type" ):
                listener.enterEntity_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntity_type" ):
                listener.exitEntity_type(self)


    class Boolean_typeContext(Type_specContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AntlrScriptParser.Type_specContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOLEAN(self):
            return self.getToken(AntlrScriptParser.BOOLEAN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolean_type" ):
                listener.enterBoolean_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolean_type" ):
                listener.exitBoolean_type(self)


    class Integer_typeContext(Type_specContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AntlrScriptParser.Type_specContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INTEGER(self):
            return self.getToken(AntlrScriptParser.INTEGER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInteger_type" ):
                listener.enterInteger_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInteger_type" ):
                listener.exitInteger_type(self)



    def type_spec(self):

        localctx = AntlrScriptParser.Type_specContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_type_spec)
        try:
            self.state = 20
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = AntlrScriptParser.Integer_typeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 16
                self.match(AntlrScriptParser.INTEGER)
                pass
            elif token in [2]:
                localctx = AntlrScriptParser.Boolean_typeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 17
                self.match(AntlrScriptParser.BOOLEAN)
                pass
            elif token in [3]:
                localctx = AntlrScriptParser.String_typeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 18
                self.match(AntlrScriptParser.STRING)
                pass
            elif token in [12]:
                localctx = AntlrScriptParser.Entity_typeContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 19
                localctx.target = self.match(AntlrScriptParser.ID)
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





