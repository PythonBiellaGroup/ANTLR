import unittest

from antlr4 import CommonTokenStream, InputStream

from entity_parser.AntlrEntityLexer import AntlrEntityLexer
from entity_parser.AntlrEntityParser import AntlrEntityParser
from script_parser.AntlrScriptLexer import AntlrScriptLexer
from script_parser.AntlrScriptParser import AntlrScriptParser


class ScriptParserTest(unittest.TestCase):
    def test_parse_module(self):
        code = '''
        create Client as c
        set name of c to 'ACME Inc.'
        create Product as p1
        set value of p1 to (1500 + 200) / 2
        print concat('Value of product #1 is: ', value of p1)
        '''
        input = InputStream(code)
        lexer = AntlrScriptLexer(input)
        token_stream = CommonTokenStream(lexer)
        parser = AntlrScriptParser(token_stream)
        tree = parser.module()
        self.assertIsInstance(tree, AntlrEntityParser.ModuleContext)
        self.assertIsInstance(tree.getChild(4), AntlrEntityParser.EntityContext)
        self.assertEqual(2, len(tree.entities))
        self.assertIsInstance(tree.entities[0], AntlrEntityParser.EntityContext)
        self.assertEqual(0, parser.getNumberOfSyntaxErrors())
