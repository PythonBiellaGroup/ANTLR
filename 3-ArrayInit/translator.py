'''
Implementiamo il traduttore
'''
from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
# Import lexer e parser della grammatica generata con ANTLR
from ArrayInitLexer import ArrayInitLexer
from ArrayInitParser import ArrayInitParser
# Import del visitor custom
from ToUnicodeListener import ToUnicodeListener

# Input da consolle, una riga sola
input_stream = InputStream(input("Lista di interi? "))

# Cattura i tokens
lexer = ArrayInitLexer(input_stream)
token_stream = CommonTokenStream(lexer)
# Li passa al parser
parser = ArrayInitParser(token_stream)
# Abstract Syntax Tree
tree = parser.init()
# Usiamo il custom listener
listener = ToUnicodeListener()
walker = ParseTreeWalker()
# Il walker esplora l'albero usando il nostro listener
walker.walk(listener, tree)