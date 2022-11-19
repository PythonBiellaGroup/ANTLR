import unittest

from pylasu.model import Position, Point
from pylasu.model.naming import ReferenceByName
from pylasu.validation.validation import Result, IssueType, IssueSeverity

from interpreter.entities_parser.entities_ast import EntityRefType
from interpreter.script_parser.script_ast import Script, SetStatement, CreateStatement, PrintStatement, \
    StringLiteralExpression, \
    IntLiteralExpression, SumExpression, DivisionExpression, GetFeatureValueExpression, ConcatExpression, \
    ReferenceExpression
from interpreter.script_parser.script_pylasu_parser import ScriptPylasuParser


class ScriptParserTest(unittest.TestCase):

    def test_pylasu_parse_simple_script(self):
        code = '''create Client as c'''
        result = ScriptPylasuParser().parse(code)
        self.assertEqual(0, len(result.issues))
        self.assertEqual(Result(issues=[], root=Script(statements=[
            CreateStatement(entity=ReferenceByName(name='Client'), name='c')])), result)

    def test_pylasu_parse_error(self):
        code = '''unknown statement'''
        result = ScriptPylasuParser().parse(code)
        self.assertEqual(1, len(result.issues))
        issue = result.issues[0]
        self.assertEqual(IssueType.SYNTACTIC, issue.type)
        self.assertEqual(IssueSeverity.ERROR, issue.severity)
        self.assertEqual(Point(line=1, column=0), issue.position.start)

    def test_pylasu_parse_advanced_script(self):
        code = '''
        create Client as c
        set name of c to 'ACME Inc.'
        create Product as p1
        set value of p1 to (1500 + 200) / 2
        print concat 'Value of product #1 is: ' and value of p1
        '''
        result = ScriptPylasuParser().parse(code)
        print(str(result.issues))
        self.assertEqual(0, len(result.issues))
        self.assertEqual(Result(issues=[], root=Script(statements=[
            CreateStatement(entity=ReferenceByName(name='Client'), name='c'),
            SetStatement(instance=ReferenceExpression(what=ReferenceByName(name='c')),
                         feature=ReferenceByName(name='name'),
                         value=StringLiteralExpression(value='ACME Inc.')),
            CreateStatement(entity=ReferenceByName(name='Product'), name='p1'),
            SetStatement(instance=ReferenceExpression(what=ReferenceByName(name='p1')),
                         feature=ReferenceByName(name='value'),
                         value=DivisionExpression(
                             left=SumExpression(
                                 left=IntLiteralExpression(value=1500),
                                 right=IntLiteralExpression(value=200),
                             ),
                             right=IntLiteralExpression(value=2)
                         )),
            PrintStatement(
                message=ConcatExpression(
                    left=StringLiteralExpression(value='Value of product #1 is: '),
                    right=GetFeatureValueExpression(
                        instance=ReferenceExpression(what=ReferenceByName(name='p1')),
                        feature=ReferenceByName(name='value'),
                    )
                )
            )]
        )), result)

    def test_pylasu_children(self):
        code = '''
        create Client as c
        set name of c to 'ACME Inc.'
        create Project as p
        set name of p to 'Amazing Project'
        print concat (concat 'Working on ' and name of p) and (concat ' for ' and name of client of p)  
        '''
        result = ScriptPylasuParser().parse(code)
        self.assertEqual(0, len(result.issues))
        self.assertEqual(5, len(list(result.root.children)))
        self.assertEqual(0, len(list(result.root.walk_descendants(restrict_to=EntityRefType))))
        self.assertEqual(3, len(list(result.root.walk_descendants(restrict_to=ConcatExpression))))

    def test_position(self):
        code = '''create Client as c
        set name of c to 'ACME Inc.'
        create Project as p
        set name of p to 'Amazing Project'
        print concat (concat 'Working on ' and name of p) and (concat ' for ' and name of client of p)'''
        result = ScriptPylasuParser().parse(code)
        self.assertEqual(0, len(result.issues))
        self.assertEqual(Position(Point(line=1, column=0), Point(line=5, column=102)), result.root.position)
        self.assertEqual(Position(Point(line=1, column=0), Point(line=1, column=18)),
                         list(result.root.children)[0].position)
