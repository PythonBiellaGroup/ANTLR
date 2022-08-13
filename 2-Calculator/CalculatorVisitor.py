# Generated from Calculator.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CalculatorParser import CalculatorParser
else:
    from CalculatorParser import CalculatorParser

# This class defines a complete generic visitor for a parse tree produced by CalculatorParser.

class CalculatorVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CalculatorParser#AtomExpr.
    def visitAtomExpr(self, ctx:CalculatorParser.AtomExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#ParenExpr.
    def visitParenExpr(self, ctx:CalculatorParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#OpExpr.
    def visitOpExpr(self, ctx:CalculatorParser.OpExprContext):
        return self.visitChildren(ctx)



del CalculatorParser