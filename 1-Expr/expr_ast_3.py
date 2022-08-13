'''
Script di test grammatica Expr
- con input da file
    Esempio: python expr_ast_3.py 3.txt
- con stampa Abstract Syntax Tree
'''
import sys
from antlr4 import FileStream, CommonTokenStream
# Import lexer e parser della grammatica generata con ANTLR
from ExprLexer import ExprLexer
from ExprParser import ExprParser

def evaluator(input_stream):
    # Cattura i tokens
    lexer = ExprLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    # Li passa al parser
    parser = ExprParser(token_stream)
    # Abstract Syntax Tree
    tree = parser.root()
    return parser, tree

if __name__ == '__main__':
    # Input da file
    input_stream = FileStream(sys.argv[1])
    parser, tree = evaluator(input_stream)
    print("AST: ",tree.toStringTree(recog=parser))
