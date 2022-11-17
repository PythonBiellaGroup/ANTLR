from antlr4 import InputStream, CommonTokenStream
from pylasu.validation.validation import Result

from entity_parser.AntlrEntityLexer import AntlrEntityLexer
from entity_parser.AntlrEntityParser import AntlrEntityParser
from interpreter.entities_parser.entities_ast import Module
from interpreter.entities_parser.entities_parsetree_converter import to_ast

class EntitiesPylasuParser:

    def parse(self, code: str) -> Result:
        input = InputStream(code)
        lexer = AntlrEntityLexer(input)
        token_stream = CommonTokenStream(lexer)
        parser = AntlrEntityParser(token_stream)
        parse_tree = parser.module()
        issues = []
        return Result(root=parse_tree.to_ast(issues), issues=issues)