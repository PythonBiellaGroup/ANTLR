# Generated from Condizioni.g by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CondizioniParser import CondizioniParser
else:
    from CondizioniParser import CondizioniParser

# This class defines a complete generic visitor for a parse tree produced by CondizioniParser.

class CondizioniVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CondizioniParser#root.
    def visitRoot(self, ctx:CondizioniParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CondizioniParser#Condition.
    def visitCondition(self, ctx:CondizioniParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CondizioniParser#Print.
    def visitPrint(self, ctx:CondizioniParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CondizioniParser#Value.
    def visitValue(self, ctx:CondizioniParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CondizioniParser#Lt.
    def visitLt(self, ctx:CondizioniParser.LtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CondizioniParser#Gt.
    def visitGt(self, ctx:CondizioniParser.GtContext):
        return self.visitChildren(ctx)



del CondizioniParser