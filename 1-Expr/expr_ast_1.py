'''
Script di test grammatica Expr
- con input da consolle singola riga
    Esempio: python expr_ast_1.py
- con stampa Abstract Syntax Tree
'''
from antlr4 import InputStream, CommonTokenStream
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
    while True:
        # Input da consolle, una riga sola
        input_stream = InputStream(input("Espressione? "))
        parser, tree = evaluator(input_stream)
        print("AST: ",tree.toStringTree(recog=parser))



