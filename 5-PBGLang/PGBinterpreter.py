'''
Interprete PBGLang
'''
import sys
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
# Import lexer e parser della grammatica generata con ANTLR
from PBGLangLexer import PBGLangLexer
from PBGLangParser import PBGLangParser
# Import del visitor custom
from PBGImplListener import PBGImplListener

# Input da consolle, una riga sola
input_stream = FileStream(sys.argv[1])

# Cattura i tokens
lexer = PBGLangLexer(input_stream)
token_stream = CommonTokenStream(lexer)
# Li passa al parser
parser = PBGLangParser(token_stream)
# Abstract Syntax Tree
tree = parser.program()
# Usiamo il custom listener
listener = PBGImplListener()
walker = ParseTreeWalker()
# Il walker esplora l'albero usando il nostro listener
walker.walk(listener, tree)