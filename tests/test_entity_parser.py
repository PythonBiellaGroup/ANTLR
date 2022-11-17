import unittest

from antlr4 import CommonTokenStream, InputStream
from pylasu.model.naming import ReferenceByName

from entity_parser.AntlrEntityLexer import AntlrEntityLexer
from entity_parser.AntlrEntityParser import AntlrEntityParser
from interpreter.entities_parser.entities_ast import Module, StringType, Entity, Feature, EntityRefType, IntegerType
from interpreter.entities_parser.entities_pylasu_parser import EntitiesPylasuParser


class EntityParserTest(unittest.TestCase):

    def test_antlr_parse_module(self):
        code = '''module Insurance {
    entity Vehicle {
        licensePlate: string;
        year: integer;
        owner: Person;
    }

    entity Person {
        name: string;
        address: string;
    }
}'''
        input = InputStream(code)
        lexer = AntlrEntityLexer(input)
        token_stream = CommonTokenStream(lexer)
        # Verifico che il quarto token sia di tipo ENTITY
        self.assertEqual(token_stream.LT(4).type, lexer.ENTITY)
        self.assertEqual(token_stream.LT(4).text, "entity")
        parser = AntlrEntityParser(token_stream)
        tree = parser.module()
        self.assertIsInstance(tree, AntlrEntityParser.ModuleContext)
        self.assertIsInstance(tree.getChild(4), AntlrEntityParser.EntityContext)
        self.assertEqual(2, len(tree.entities))
        self.assertIsInstance(tree.entities[0], AntlrEntityParser.EntityContext)
        self.assertEqual(0, parser.getNumberOfSyntaxErrors())

    def test_pylasu_parse_module(self):
        code = '''module Insurance {
    entity Vehicle {
        licensePlate: string;
        year: integer;
        owner: Person;
    }

    entity Person {
        name: string;
        address: string;
    }
}'''
        result = EntitiesPylasuParser().parse(code)
        self.assertEqual([], result.issues)
        person = Entity(name='Person',
                        features=[
                            Feature(name='name', type=StringType()),
                            Feature(name='address', type=StringType()),
                        ])
        vehicle = Entity(name='Vehicle',
                         features=[
                             Feature(name='licensePlate', type=StringType()),
                             Feature(name='year', type=IntegerType()),
                             Feature(name='owner', type=EntityRefType(entity=ReferenceByName(name='Person'))),
                         ])
        self.assertEqual(Module(
            name='Insurance',
            entities=[
                vehicle,
                person
            ]
        ), result.root)
