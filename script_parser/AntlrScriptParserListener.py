# Generated from AntlrScriptParser.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .AntlrScriptParser import AntlrScriptParser
else:
    from AntlrScriptParser import AntlrScriptParser

# This class defines a complete listener for a parse tree produced by AntlrScriptParser.
class AntlrScriptParserListener(ParseTreeListener):

    # Enter a parse tree produced by AntlrScriptParser#script.
    def enterScript(self, ctx:AntlrScriptParser.ScriptContext):
        pass

    # Exit a parse tree produced by AntlrScriptParser#script.
    def exitScript(self, ctx:AntlrScriptParser.ScriptContext):
        pass


    # Enter a parse tree produced by AntlrScriptParser#statement.
    def enterStatement(self, ctx:AntlrScriptParser.StatementContext):
        pass

    # Exit a parse tree produced by AntlrScriptParser#statement.
    def exitStatement(self, ctx:AntlrScriptParser.StatementContext):
        pass


    # Enter a parse tree produced by AntlrScriptParser#integer_type.
    def enterInteger_type(self, ctx:AntlrScriptParser.Integer_typeContext):
        pass

    # Exit a parse tree produced by AntlrScriptParser#integer_type.
    def exitInteger_type(self, ctx:AntlrScriptParser.Integer_typeContext):
        pass


    # Enter a parse tree produced by AntlrScriptParser#boolean_type.
    def enterBoolean_type(self, ctx:AntlrScriptParser.Boolean_typeContext):
        pass

    # Exit a parse tree produced by AntlrScriptParser#boolean_type.
    def exitBoolean_type(self, ctx:AntlrScriptParser.Boolean_typeContext):
        pass


    # Enter a parse tree produced by AntlrScriptParser#string_type.
    def enterString_type(self, ctx:AntlrScriptParser.String_typeContext):
        pass

    # Exit a parse tree produced by AntlrScriptParser#string_type.
    def exitString_type(self, ctx:AntlrScriptParser.String_typeContext):
        pass


    # Enter a parse tree produced by AntlrScriptParser#entity_type.
    def enterEntity_type(self, ctx:AntlrScriptParser.Entity_typeContext):
        pass

    # Exit a parse tree produced by AntlrScriptParser#entity_type.
    def exitEntity_type(self, ctx:AntlrScriptParser.Entity_typeContext):
        pass



del AntlrScriptParser