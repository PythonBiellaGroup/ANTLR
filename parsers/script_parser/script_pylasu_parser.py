from typing import List

from antlr4 import InputStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
from pylasu.model import Position, Point
from pylasu.validation.validation import Result, Issue, IssueType

from parsers.script_parser.AntlrScriptLexer import AntlrScriptLexer
from parsers.script_parser.AntlrScriptParser import AntlrScriptParser


class MyListener(ErrorListener):
    issues: List[Issue]
    issue_type: IssueType

    def __init__(self, issues: List[Issue], issue_type: IssueType):
        self.issues = issues
        self.issue_type = issue_type

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.issues.append(Issue(message=str(msg),
                                 type=self.issue_type, position=Position(start=Point(line=line, column=column),
                                                                         end=Point(line=line, column=column))))

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        pass

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        pass

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        pass


class ScriptPylasuParser:

    def parse(self, code: str) -> Result:
        issues = []

        input = InputStream(code)

        lexer = AntlrScriptLexer(input)
        lexer.removeErrorListeners()
        lexer.addErrorListener(MyListener(issues, IssueType.LEXICAL))

        token_stream = CommonTokenStream(lexer)
        parser = AntlrScriptParser(token_stream)
        parser.removeErrorListeners()
        parser.addErrorListener(MyListener(issues, IssueType.SYNTACTIC))
        parse_tree = parser.script()

        ast = parse_tree.to_ast(issues)
        ast.assign_parents()

        return Result(root=ast, issues=issues)
