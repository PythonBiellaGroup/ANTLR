'''
Prova grammatica con AST
'''
from antlr4 import InputStream, CommonTokenStream
# Import lexer e parser della grammatica generata con ANTLR
from ArrayInitLexer import ArrayInitLexer
from ArrayInitParser import ArrayInitParser

# Input da consolle, una riga sola
input_stream = InputStream(input("Lista di interi? "))

# Cattura i tokens
lexer = ArrayInitLexer(input_stream)
token_stream = CommonTokenStream(lexer)
# Li passa al parser
parser = ArrayInitParser(token_stream)
# Abstract Syntax Tree
tree = parser.init()
print("AST: ",tree.toStringTree(recog=parser))