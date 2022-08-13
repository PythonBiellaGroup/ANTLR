'''
Listener che converte un array di int in sequenza di unicode tra apici
'''
from ArrayInitListener import ArrayInitListener
from ArrayInitParser import ArrayInitParser

class ToUnicodeListener(ArrayInitListener):
    # Enter a parse tree produced by ArrayInitParser#init.
    def enterInit(self, ctx:ArrayInitParser.InitContext):
        print('"', end='')

    # Exit a parse tree produced by ArrayInitParser#init.
    def exitInit(self, ctx:ArrayInitParser.InitContext):
        print('"', end='')

    # Enter a parse tree produced by ArrayInitParser#value.
    def enterValue(self, ctx:ArrayInitParser.ValueContext):
        val = str(int(ctx.getText())).encode("utf-8")
        print(val, end='')