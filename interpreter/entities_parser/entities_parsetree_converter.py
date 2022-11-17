from pylasu.model.naming import ReferenceByName
from pylasu.support import extension_method
from pylasu.validation import Issue

from interpreter.entities_parser.entities_ast import Module, Entity, Feature, StringType, IntegerType, EntityRefType
from entity_parser.AntlrEntityParser import AntlrEntityParser


@extension_method(AntlrEntityParser.ModuleContext)
def to_ast(self: AntlrEntityParser.ModuleContext, issues: list[Issue]) -> Module:
    return Module(name=self.name.text, entities=[c.to_ast(issues) for c in self.entities])


@extension_method(AntlrEntityParser.EntityContext)
def to_ast(self: AntlrEntityParser.EntityContext, issues: list[Issue]) -> Entity:
    return Entity(name=self.name.text, features=[c.to_ast(issues) for c in self.features])


@extension_method(AntlrEntityParser.FeatureContext)
def to_ast(self: AntlrEntityParser.FeatureContext, issues: list[Issue]) -> Feature:
    return Feature(name=self.name.text, type=self.type_.to_ast(issues))


@extension_method(AntlrEntityParser.Type_specContext)
def to_ast(self: AntlrEntityParser.Type_specContext, issues: list[Issue]) -> Feature:
    if isinstance(self, AntlrEntityParser.String_typeContext):
        return StringType()
    elif isinstance(self, AntlrEntityParser.Integer_typeContext):
        return IntegerType()
    elif isinstance(self, AntlrEntityParser.Entity_typeContext):
        return EntityRefType(entity=ReferenceByName(name=self.target.text))
    else:
        raise Exception("Unsupported: %s" % str(type(self)))