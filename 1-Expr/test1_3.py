'''
Script di test grammatica Expr
- con input da file
    Esempio: python test1_3.py 1_3.txt
- con stampa Abstract Syntax Tree
'''
import sys
from antlr4 import FileStream, CommonTokenStream
# Import lexer e parser della grammatica generata con ANTLR
from ExprLexer import ExprLexer
from ExprParser import ExprParser

# Input da consolle, una riga sola
input_stream = FileStream(sys.argv[1])

# Cattura i tokens
lexer = ExprLexer(input_stream)
token_stream = CommonTokenStream(lexer)
# Li passa al parser
parser = ExprParser(token_stream)
# Abstract Syntax Tree
tree = parser.root()

print("AST: ",tree.toStringTree(recog=parser))

