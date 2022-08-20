from antlr4 import FileStream,CommonTokenStream
from CondizioniLexer import CondizioniLexer
from CondizioniParser import CondizioniParser
from InterpreteVisitor import InterpreteVisitor
import sys

# Input da file
input_stream = FileStream(sys.argv[1])

lexer = CondizioniLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = CondizioniParser(token_stream)
tree = parser.root()

# Usiamo il custom visitor
visitor = InterpreteVisitor()
visitor.visit(tree)
