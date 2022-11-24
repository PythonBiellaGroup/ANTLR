from typing import List

from pylasu.model.naming import ReferenceByName
from pylasu.parsing.parse_tree import ParseTreeOrigin
from pylasu.support import extension_method
from pylasu.validation import Issue

from interpreter.entities_parser.entities_ast import Module, Entity, Feature, StringType, IntegerType, EntityRefType
from entity_parser.AntlrEntityParser import AntlrEntityParser


@extension_method(AntlrEntityParser.ModuleContext)
def to_ast(self: AntlrEntityParser.ModuleContext, issues: List[Issue]) -> Module:
    return Module(name=self.name.text, entities=[c.to_ast(issues) for c in self.entities]).with_origin(ParseTreeOrigin(self))


@extension_method(AntlrEntityParser.EntityContext)
def to_ast(self: AntlrEntityParser.EntityContext, issues: List[Issue]) -> Entity:
    return Entity(name=self.name.text, features=[c.to_ast(issues) for c in self.features]).with_origin(ParseTreeOrigin(self))


@extension_method(AntlrEntityParser.FeatureContext)
def to_ast(self: AntlrEntityParser.FeatureContext, issues: List[Issue]) -> Feature:
    return Feature(name=self.name.text, type=self.type_.to_ast(issues)).with_origin(ParseTreeOrigin(self))


@extension_method(AntlrEntityParser.Type_specContext)
def to_ast(self: AntlrEntityParser.Type_specContext, issues: List[Issue]) -> Feature:
    if isinstance(self, AntlrEntityParser.String_typeContext):
        return StringType().with_origin(ParseTreeOrigin(self))
    elif isinstance(self, AntlrEntityParser.Integer_typeContext):
        return IntegerType().with_origin(ParseTreeOrigin(self))
    elif isinstance(self, AntlrEntityParser.Entity_typeContext):
        return EntityRefType(entity=ReferenceByName(name=self.target.text)).with_origin(ParseTreeOrigin(self))
    else:
        raise Exception("Unsupported: %s" % str(type(self)))
