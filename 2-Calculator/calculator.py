#!/usr/bin/python3
import sys
from antlr4 import InputStream, CommonTokenStream
from CalculatorLexer import CalculatorLexer
from CalculatorParser import CalculatorParser
from EvalVisitor import EvalVisitor

def calculator(line) -> float:
    input_stream = InputStream(line)

    # lexing
    lexer = CalculatorLexer(input_stream)
    stream = CommonTokenStream(lexer)

    # parsing
    parser = CalculatorParser(stream)
    tree = parser.expr()

    # use customized visitor to traverse AST
    visitor = EvalVisitor()
    return visitor.visit(tree)


if __name__ == '__main__':
    while True:
        print(">>> ", end='')
        line = input()
        print(calculator(line))
