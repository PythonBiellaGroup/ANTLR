# Generated from AntlrEntityParser.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .AntlrEntityParser import AntlrEntityParser
else:
    from AntlrEntityParser import AntlrEntityParser

# This class defines a complete listener for a parse tree produced by AntlrEntityParser.
class AntlrEntityParserListener(ParseTreeListener):

    # Enter a parse tree produced by AntlrEntityParser#module.
    def enterModule(self, ctx:AntlrEntityParser.ModuleContext):
        pass

    # Exit a parse tree produced by AntlrEntityParser#module.
    def exitModule(self, ctx:AntlrEntityParser.ModuleContext):
        pass


    # Enter a parse tree produced by AntlrEntityParser#entity.
    def enterEntity(self, ctx:AntlrEntityParser.EntityContext):
        pass

    # Exit a parse tree produced by AntlrEntityParser#entity.
    def exitEntity(self, ctx:AntlrEntityParser.EntityContext):
        pass


    # Enter a parse tree produced by AntlrEntityParser#feature.
    def enterFeature(self, ctx:AntlrEntityParser.FeatureContext):
        pass

    # Exit a parse tree produced by AntlrEntityParser#feature.
    def exitFeature(self, ctx:AntlrEntityParser.FeatureContext):
        pass


    # Enter a parse tree produced by AntlrEntityParser#integer_type.
    def enterInteger_type(self, ctx:AntlrEntityParser.Integer_typeContext):
        pass

    # Exit a parse tree produced by AntlrEntityParser#integer_type.
    def exitInteger_type(self, ctx:AntlrEntityParser.Integer_typeContext):
        pass


    # Enter a parse tree produced by AntlrEntityParser#boolean_type.
    def enterBoolean_type(self, ctx:AntlrEntityParser.Boolean_typeContext):
        pass

    # Exit a parse tree produced by AntlrEntityParser#boolean_type.
    def exitBoolean_type(self, ctx:AntlrEntityParser.Boolean_typeContext):
        pass


    # Enter a parse tree produced by AntlrEntityParser#string_type.
    def enterString_type(self, ctx:AntlrEntityParser.String_typeContext):
        pass

    # Exit a parse tree produced by AntlrEntityParser#string_type.
    def exitString_type(self, ctx:AntlrEntityParser.String_typeContext):
        pass


    # Enter a parse tree produced by AntlrEntityParser#entity_type.
    def enterEntity_type(self, ctx:AntlrEntityParser.Entity_typeContext):
        pass

    # Exit a parse tree produced by AntlrEntityParser#entity_type.
    def exitEntity_type(self, ctx:AntlrEntityParser.Entity_typeContext):
        pass



del AntlrEntityParser