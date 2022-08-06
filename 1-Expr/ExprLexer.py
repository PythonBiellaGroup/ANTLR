# Generated from Expr.g by ANTLR 4.10.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,3,18,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,1,0,4,0,9,8,0,11,0,12,0,10,
        1,1,1,1,1,2,1,2,1,2,1,2,0,0,3,1,1,3,2,5,3,1,0,2,1,0,48,57,2,0,10,
        10,32,32,18,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,1,8,1,0,0,0,3,12,
        1,0,0,0,5,14,1,0,0,0,7,9,7,0,0,0,8,7,1,0,0,0,9,10,1,0,0,0,10,8,1,
        0,0,0,10,11,1,0,0,0,11,2,1,0,0,0,12,13,5,43,0,0,13,4,1,0,0,0,14,
        15,7,1,0,0,15,16,1,0,0,0,16,17,6,2,0,0,17,6,1,0,0,0,2,0,10,1,6,0,
        0
    ]

class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NUM = 1
    PLUS = 2
    WS = 3

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'" ]

    symbolicNames = [ "<INVALID>",
            "NUM", "PLUS", "WS" ]

    ruleNames = [ "NUM", "PLUS", "WS" ]

    grammarFileName = "Expr.g"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


