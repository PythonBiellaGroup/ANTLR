# Generated from PBGLang.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PBGLangParser import PBGLangParser
else:
    from PBGLangParser import PBGLangParser

# This class defines a complete listener for a parse tree produced by PBGLangParser.
class PBGLangListener(ParseTreeListener):

    # Enter a parse tree produced by PBGLangParser#program.
    def enterProgram(self, ctx:PBGLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by PBGLangParser#program.
    def exitProgram(self, ctx:PBGLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by PBGLangParser#statement.
    def enterStatement(self, ctx:PBGLangParser.StatementContext):
        pass

    # Exit a parse tree produced by PBGLangParser#statement.
    def exitStatement(self, ctx:PBGLangParser.StatementContext):
        pass


    # Enter a parse tree produced by PBGLangParser#let.
    def enterLet(self, ctx:PBGLangParser.LetContext):
        pass

    # Exit a parse tree produced by PBGLangParser#let.
    def exitLet(self, ctx:PBGLangParser.LetContext):
        pass


    # Enter a parse tree produced by PBGLangParser#show.
    def enterShow(self, ctx:PBGLangParser.ShowContext):
        pass

    # Exit a parse tree produced by PBGLangParser#show.
    def exitShow(self, ctx:PBGLangParser.ShowContext):
        pass



del PBGLangParser