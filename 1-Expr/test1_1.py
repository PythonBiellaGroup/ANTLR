'''
Script di test grammatica Expr
- con input da consolle singola riga
- con stampa Abstract Syntax Tree
'''
from antlr4 import InputStream, CommonTokenStream
# Import lexer e parser della grammatica generata con ANTLR
from ExprLexer import ExprLexer
from ExprParser import ExprParser

# Input da consolle, una riga sola
input_stream = InputStream(input("Espressione? "))

# Cattura i tokens
lexer = ExprLexer(input_stream)
token_stream = CommonTokenStream(lexer)
# Li passa al parser
parser = ExprParser(token_stream)
# Abstract Syntax Tree
tree = parser.root()

print("AST: ",tree.toStringTree(recog=parser))

