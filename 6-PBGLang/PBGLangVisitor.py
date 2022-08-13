# Generated from PBGLang.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PBGLangParser import PBGLangParser
else:
    from PBGLangParser import PBGLangParser

# This class defines a complete generic visitor for a parse tree produced by PBGLangParser.

class PBGLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PBGLangParser#program.
    def visitProgram(self, ctx:PBGLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PBGLangParser#statement.
    def visitStatement(self, ctx:PBGLangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PBGLangParser#let.
    def visitLet(self, ctx:PBGLangParser.LetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PBGLangParser#show.
    def visitShow(self, ctx:PBGLangParser.ShowContext):
        return self.visitChildren(ctx)



del PBGLangParser