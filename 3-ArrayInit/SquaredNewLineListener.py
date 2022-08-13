'''
Listener che converte un array di int in sequenza di unicode tra apici
'''
from ArrayInitListener import ArrayInitListener
from ArrayInitParser import ArrayInitParser

class SquaredNewLineListener(ArrayInitListener):
    # Enter a parse tree produced by ArrayInitParser#init.
    def enterInit(self, ctx:ArrayInitParser.InitContext):
        print('[')

    # Exit a parse tree produced by ArrayInitParser#init.
    def exitInit(self, ctx:ArrayInitParser.InitContext):
        print(']')

    # Enter a parse tree produced by ArrayInitParser#value.
    def enterValue(self, ctx:ArrayInitParser.ValueContext):
        print(ctx.getText())