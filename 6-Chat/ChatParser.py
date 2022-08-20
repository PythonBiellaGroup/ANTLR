# Generated from Chat.g4 by ANTLR 4.10.1
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
        4,1,14,76,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,4,0,20,8,0,11,0,12,0,21,1,0,1,0,1,1,1,1,1,
        1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,4,2,37,8,2,11,2,12,2,38,1,3,1,
        3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,3,5,50,8,5,1,5,1,5,1,5,3,5,55,8,5,
        1,5,3,5,58,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,
        7,1,8,1,8,1,8,1,8,0,0,9,0,2,4,6,8,10,12,14,16,0,1,1,0,9,10,76,0,
        19,1,0,0,0,2,25,1,0,0,0,4,36,1,0,0,0,6,40,1,0,0,0,8,43,1,0,0,0,10,
        57,1,0,0,0,12,59,1,0,0,0,14,66,1,0,0,0,16,72,1,0,0,0,18,20,3,2,1,
        0,19,18,1,0,0,0,20,21,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,23,
        1,0,0,0,23,24,5,0,0,1,24,1,1,0,0,0,25,26,3,6,3,0,26,27,3,8,4,0,27,
        28,3,4,2,0,28,29,5,14,0,0,29,3,1,0,0,0,30,37,3,10,5,0,31,37,3,12,
        6,0,32,37,3,14,7,0,33,37,3,16,8,0,34,37,5,12,0,0,35,37,5,13,0,0,
        36,30,1,0,0,0,36,31,1,0,0,0,36,32,1,0,0,0,36,33,1,0,0,0,36,34,1,
        0,0,0,36,35,1,0,0,0,37,38,1,0,0,0,38,36,1,0,0,0,38,39,1,0,0,0,39,
        5,1,0,0,0,40,41,5,12,0,0,41,42,5,13,0,0,42,7,1,0,0,0,43,44,7,0,0,
        0,44,45,5,1,0,0,45,46,5,13,0,0,46,9,1,0,0,0,47,49,5,1,0,0,48,50,
        5,2,0,0,49,48,1,0,0,0,49,50,1,0,0,0,50,51,1,0,0,0,51,58,5,3,0,0,
        52,54,5,1,0,0,53,55,5,2,0,0,54,53,1,0,0,0,54,55,1,0,0,0,55,56,1,
        0,0,0,56,58,5,4,0,0,57,47,1,0,0,0,57,52,1,0,0,0,58,11,1,0,0,0,59,
        60,5,5,0,0,60,61,5,11,0,0,61,62,5,6,0,0,62,63,5,4,0,0,63,64,5,11,
        0,0,64,65,5,3,0,0,65,13,1,0,0,0,66,67,5,7,0,0,67,68,5,12,0,0,68,
        69,5,7,0,0,69,70,3,4,2,0,70,71,5,7,0,0,71,15,1,0,0,0,72,73,5,8,0,
        0,73,74,5,12,0,0,74,17,1,0,0,0,6,21,36,38,49,54,57
    ]

class ChatParser ( Parser ):

    grammarFileName = "Chat.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'-'", "')'", "'('", "'['", "']'", 
                     "'/'", "'@'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "SAYS", "SHOUTS", "TEXT", "WORD", "WHITESPACE", 
                      "NEWLINE" ]

    RULE_chat = 0
    RULE_line = 1
    RULE_message = 2
    RULE_name = 3
    RULE_command = 4
    RULE_emoticon = 5
    RULE_link = 6
    RULE_color = 7
    RULE_mention = 8

    ruleNames =  [ "chat", "line", "message", "name", "command", "emoticon", 
                   "link", "color", "mention" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    SAYS=9
    SHOUTS=10
    TEXT=11
    WORD=12
    WHITESPACE=13
    NEWLINE=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ChatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ChatParser.EOF, 0)

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChatParser.LineContext)
            else:
                return self.getTypedRuleContext(ChatParser.LineContext,i)


        def getRuleIndex(self):
            return ChatParser.RULE_chat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChat" ):
                listener.enterChat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChat" ):
                listener.exitChat(self)




    def chat(self):

        localctx = ChatParser.ChatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_chat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.line()
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ChatParser.WORD):
                    break

            self.state = 23
            self.match(ChatParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(ChatParser.NameContext,0)


        def command(self):
            return self.getTypedRuleContext(ChatParser.CommandContext,0)


        def message(self):
            return self.getTypedRuleContext(ChatParser.MessageContext,0)


        def NEWLINE(self):
            return self.getToken(ChatParser.NEWLINE, 0)

        def getRuleIndex(self):
            return ChatParser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)




    def line(self):

        localctx = ChatParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.name()
            self.state = 26
            self.command()
            self.state = 27
            self.message()
            self.state = 28
            self.match(ChatParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MessageContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def emoticon(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChatParser.EmoticonContext)
            else:
                return self.getTypedRuleContext(ChatParser.EmoticonContext,i)


        def link(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChatParser.LinkContext)
            else:
                return self.getTypedRuleContext(ChatParser.LinkContext,i)


        def color(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChatParser.ColorContext)
            else:
                return self.getTypedRuleContext(ChatParser.ColorContext,i)


        def mention(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChatParser.MentionContext)
            else:
                return self.getTypedRuleContext(ChatParser.MentionContext,i)


        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(ChatParser.WORD)
            else:
                return self.getToken(ChatParser.WORD, i)

        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(ChatParser.WHITESPACE)
            else:
                return self.getToken(ChatParser.WHITESPACE, i)

        def getRuleIndex(self):
            return ChatParser.RULE_message

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMessage" ):
                listener.enterMessage(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMessage" ):
                listener.exitMessage(self)




    def message(self):

        localctx = ChatParser.MessageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_message)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 36
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [ChatParser.T__0]:
                        self.state = 30
                        self.emoticon()
                        pass
                    elif token in [ChatParser.T__4]:
                        self.state = 31
                        self.link()
                        pass
                    elif token in [ChatParser.T__6]:
                        self.state = 32
                        self.color()
                        pass
                    elif token in [ChatParser.T__7]:
                        self.state = 33
                        self.mention()
                        pass
                    elif token in [ChatParser.WORD]:
                        self.state = 34
                        self.match(ChatParser.WORD)
                        pass
                    elif token in [ChatParser.WHITESPACE]:
                        self.state = 35
                        self.match(ChatParser.WHITESPACE)
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 38 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(ChatParser.WORD, 0)

        def WHITESPACE(self):
            return self.getToken(ChatParser.WHITESPACE, 0)

        def getRuleIndex(self):
            return ChatParser.RULE_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName" ):
                listener.enterName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName" ):
                listener.exitName(self)




    def name(self):

        localctx = ChatParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(ChatParser.WORD)
            self.state = 41
            self.match(ChatParser.WHITESPACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHITESPACE(self):
            return self.getToken(ChatParser.WHITESPACE, 0)

        def SAYS(self):
            return self.getToken(ChatParser.SAYS, 0)

        def SHOUTS(self):
            return self.getToken(ChatParser.SHOUTS, 0)

        def getRuleIndex(self):
            return ChatParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)




    def command(self):

        localctx = ChatParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_command)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            _la = self._input.LA(1)
            if not(_la==ChatParser.SAYS or _la==ChatParser.SHOUTS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 44
            self.match(ChatParser.T__0)
            self.state = 45
            self.match(ChatParser.WHITESPACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EmoticonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ChatParser.RULE_emoticon

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmoticon" ):
                listener.enterEmoticon(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmoticon" ):
                listener.exitEmoticon(self)




    def emoticon(self):

        localctx = ChatParser.EmoticonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_emoticon)
        self._la = 0 # Token type
        try:
            self.state = 57
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.match(ChatParser.T__0)
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ChatParser.T__1:
                    self.state = 48
                    self.match(ChatParser.T__1)


                self.state = 51
                self.match(ChatParser.T__2)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.match(ChatParser.T__0)
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ChatParser.T__1:
                    self.state = 53
                    self.match(ChatParser.T__1)


                self.state = 56
                self.match(ChatParser.T__3)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LinkContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self, i:int=None):
            if i is None:
                return self.getTokens(ChatParser.TEXT)
            else:
                return self.getToken(ChatParser.TEXT, i)

        def getRuleIndex(self):
            return ChatParser.RULE_link

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLink" ):
                listener.enterLink(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLink" ):
                listener.exitLink(self)




    def link(self):

        localctx = ChatParser.LinkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_link)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(ChatParser.T__4)
            self.state = 60
            self.match(ChatParser.TEXT)
            self.state = 61
            self.match(ChatParser.T__5)
            self.state = 62
            self.match(ChatParser.T__3)
            self.state = 63
            self.match(ChatParser.TEXT)
            self.state = 64
            self.match(ChatParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(ChatParser.WORD, 0)

        def message(self):
            return self.getTypedRuleContext(ChatParser.MessageContext,0)


        def getRuleIndex(self):
            return ChatParser.RULE_color

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColor" ):
                listener.enterColor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColor" ):
                listener.exitColor(self)




    def color(self):

        localctx = ChatParser.ColorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_color)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(ChatParser.T__6)
            self.state = 67
            self.match(ChatParser.WORD)
            self.state = 68
            self.match(ChatParser.T__6)
            self.state = 69
            self.message()
            self.state = 70
            self.match(ChatParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MentionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(ChatParser.WORD, 0)

        def getRuleIndex(self):
            return ChatParser.RULE_mention

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMention" ):
                listener.enterMention(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMention" ):
                listener.exitMention(self)




    def mention(self):

        localctx = ChatParser.MentionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_mention)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(ChatParser.T__7)
            self.state = 73
            self.match(ChatParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





