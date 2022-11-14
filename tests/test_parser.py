import unittest

from antlr4 import CommonTokenStream, InputStream

from entity_parser.AntlrEntityLexer import AntlrEntityLexer
from entity_parser.AntlrEntityParser import AntlrEntityParser


class ParserTest(unittest.TestCase):
    def test_parse_module(self):
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
        self.assertEqual(0, parser.getNumberOfSyntaxErrors())
