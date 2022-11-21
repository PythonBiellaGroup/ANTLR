# Generated from AntlrEntityParser.g4 by ANTLR 4.11.1
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
        4,1,13,43,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,0,5,0,13,
        8,0,10,0,12,0,16,9,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,5,1,25,8,1,10,1,
        12,1,28,9,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,41,8,
        3,1,3,0,0,4,0,2,4,6,0,0,43,0,8,1,0,0,0,2,20,1,0,0,0,4,31,1,0,0,0,
        6,40,1,0,0,0,8,9,5,5,0,0,9,10,5,12,0,0,10,14,5,10,0,0,11,13,3,2,
        1,0,12,11,1,0,0,0,13,16,1,0,0,0,14,12,1,0,0,0,14,15,1,0,0,0,15,17,
        1,0,0,0,16,14,1,0,0,0,17,18,5,11,0,0,18,19,5,0,0,1,19,1,1,0,0,0,
        20,21,5,4,0,0,21,22,5,12,0,0,22,26,5,10,0,0,23,25,3,4,2,0,24,23,
        1,0,0,0,25,28,1,0,0,0,26,24,1,0,0,0,26,27,1,0,0,0,27,29,1,0,0,0,
        28,26,1,0,0,0,29,30,5,11,0,0,30,3,1,0,0,0,31,32,5,12,0,0,32,33,5,
        6,0,0,33,34,3,6,3,0,34,35,5,7,0,0,35,5,1,0,0,0,36,41,5,1,0,0,37,
        41,5,2,0,0,38,41,5,3,0,0,39,41,5,12,0,0,40,36,1,0,0,0,40,37,1,0,
        0,0,40,38,1,0,0,0,40,39,1,0,0,0,41,7,1,0,0,0,3,14,26,40
    ]

class AntlrEntityParser ( Parser ):

    grammarFileName = "AntlrEntityParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'integer'", "'boolean'", "'string'", 
                     "'entity'", "'module'", "':'", "';'", "'['", "']'", 
                     "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "INTEGER", "BOOLEAN", "STRING", "ENTITY", 
                      "MODULE", "COLON", "SEMI", "LSQRD", "RSQRD", "LCRLY", 
                      "RCRLY", "ID", "WS" ]

    RULE_module = 0
    RULE_entity = 1
    RULE_feature = 2
    RULE_type_spec = 3

    ruleNames =  [ "module", "entity", "feature", "type_spec" ]

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

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ModuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token
            self._entity = None # EntityContext
            self.entities = list() # of EntityContexts

        def MODULE(self):
            return self.getToken(AntlrEntityParser.MODULE, 0)

        def LCRLY(self):
            return self.getToken(AntlrEntityParser.LCRLY, 0)

        def RCRLY(self):
            return self.getToken(AntlrEntityParser.RCRLY, 0)

        def EOF(self):
            return self.getToken(AntlrEntityParser.EOF, 0)

        def ID(self):
            return self.getToken(AntlrEntityParser.ID, 0)

        def entity(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AntlrEntityParser.EntityContext)
            else:
                return self.getTypedRuleContext(AntlrEntityParser.EntityContext,i)


        def getRuleIndex(self):
            return AntlrEntityParser.RULE_module

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModule" ):
                listener.enterModule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModule" ):
                listener.exitModule(self)




    def module(self):

        localctx = AntlrEntityParser.ModuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_module)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.match(AntlrEntityParser.MODULE)
            self.state = 9
            localctx.name = self.match(AntlrEntityParser.ID)
            self.state = 10
            self.match(AntlrEntityParser.LCRLY)
            self.state = 14
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 11
                localctx._entity = self.entity()
                localctx.entities.append(localctx._entity)
                self.state = 16
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 17
            self.match(AntlrEntityParser.RCRLY)
            self.state = 18
            self.match(AntlrEntityParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EntityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token
            self._feature = None # FeatureContext
            self.features = list() # of FeatureContexts

        def ENTITY(self):
            return self.getToken(AntlrEntityParser.ENTITY, 0)

        def LCRLY(self):
            return self.getToken(AntlrEntityParser.LCRLY, 0)

        def RCRLY(self):
            return self.getToken(AntlrEntityParser.RCRLY, 0)

        def ID(self):
            return self.getToken(AntlrEntityParser.ID, 0)

        def feature(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AntlrEntityParser.FeatureContext)
            else:
                return self.getTypedRuleContext(AntlrEntityParser.FeatureContext,i)


        def getRuleIndex(self):
            return AntlrEntityParser.RULE_entity

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntity" ):
                listener.enterEntity(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntity" ):
                listener.exitEntity(self)




    def entity(self):

        localctx = AntlrEntityParser.EntityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_entity)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.match(AntlrEntityParser.ENTITY)
            self.state = 21
            localctx.name = self.match(AntlrEntityParser.ID)
            self.state = 22
            self.match(AntlrEntityParser.LCRLY)
            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 23
                localctx._feature = self.feature()
                localctx.features.append(localctx._feature)
                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 29
            self.match(AntlrEntityParser.RCRLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FeatureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token
            self.type_ = None # Type_specContext

        def COLON(self):
            return self.getToken(AntlrEntityParser.COLON, 0)

        def SEMI(self):
            return self.getToken(AntlrEntityParser.SEMI, 0)

        def ID(self):
            return self.getToken(AntlrEntityParser.ID, 0)

        def type_spec(self):
            return self.getTypedRuleContext(AntlrEntityParser.Type_specContext,0)


        def getRuleIndex(self):
            return AntlrEntityParser.RULE_feature

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFeature" ):
                listener.enterFeature(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFeature" ):
                listener.exitFeature(self)




    def feature(self):

        localctx = AntlrEntityParser.FeatureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_feature)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            localctx.name = self.match(AntlrEntityParser.ID)
            self.state = 32
            self.match(AntlrEntityParser.COLON)
            self.state = 33
            localctx.type_ = self.type_spec()
            self.state = 34
            self.match(AntlrEntityParser.SEMI)
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
            return AntlrEntityParser.RULE_type_spec

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class String_typeContext(Type_specContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AntlrEntityParser.Type_specContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(AntlrEntityParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString_type" ):
                listener.enterString_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString_type" ):
                listener.exitString_type(self)


    class Entity_typeContext(Type_specContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AntlrEntityParser.Type_specContext
            super().__init__(parser)
            self.target = None # Token
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(AntlrEntityParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntity_type" ):
                listener.enterEntity_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntity_type" ):
                listener.exitEntity_type(self)


    class Boolean_typeContext(Type_specContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AntlrEntityParser.Type_specContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOLEAN(self):
            return self.getToken(AntlrEntityParser.BOOLEAN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolean_type" ):
                listener.enterBoolean_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolean_type" ):
                listener.exitBoolean_type(self)


    class Integer_typeContext(Type_specContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AntlrEntityParser.Type_specContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INTEGER(self):
            return self.getToken(AntlrEntityParser.INTEGER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInteger_type" ):
                listener.enterInteger_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInteger_type" ):
                listener.exitInteger_type(self)



    def type_spec(self):

        localctx = AntlrEntityParser.Type_specContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_type_spec)
        try:
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = AntlrEntityParser.Integer_typeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self.match(AntlrEntityParser.INTEGER)
                pass
            elif token in [2]:
                localctx = AntlrEntityParser.Boolean_typeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 37
                self.match(AntlrEntityParser.BOOLEAN)
                pass
            elif token in [3]:
                localctx = AntlrEntityParser.String_typeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 38
                self.match(AntlrEntityParser.STRING)
                pass
            elif token in [12]:
                localctx = AntlrEntityParser.Entity_typeContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 39
                localctx.target = self.match(AntlrEntityParser.ID)
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





