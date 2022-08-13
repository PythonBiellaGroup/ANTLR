# Generated from JSON.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JSONParser import JSONParser
else:
    from JSONParser import JSONParser

# This class defines a complete generic visitor for a parse tree produced by JSONParser.

class JSONVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by JSONParser#json.
    def visitJson(self, ctx:JSONParser.JsonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSONParser#AnObject.
    def visitAnObject(self, ctx:JSONParser.AnObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSONParser#EmptyObject.
    def visitEmptyObject(self, ctx:JSONParser.EmptyObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSONParser#pair.
    def visitPair(self, ctx:JSONParser.PairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSONParser#ArrayOfValues.
    def visitArrayOfValues(self, ctx:JSONParser.ArrayOfValuesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSONParser#EmptyArray.
    def visitEmptyArray(self, ctx:JSONParser.EmptyArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSONParser#String.
    def visitString(self, ctx:JSONParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSONParser#Atom.
    def visitAtom(self, ctx:JSONParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSONParser#ObjectValue.
    def visitObjectValue(self, ctx:JSONParser.ObjectValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSONParser#ArrayValue.
    def visitArrayValue(self, ctx:JSONParser.ArrayValueContext):
        return self.visitChildren(ctx)



del JSONParser