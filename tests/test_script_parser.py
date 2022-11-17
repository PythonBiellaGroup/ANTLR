import unittest

from pylasu.model.naming import ReferenceByName
from pylasu.validation.validation import Result

from interpreter.script_parser.script_ast import Script, SetStatement, CreateStatement, PrintStatement, StringLiteralExpression, \
    IntLiteralExpression, SumExpression, DivisionExpression, GetFeatureValueExpression, ConcatExpression, \
    ReferenceExpression
from interpreter.script_parser.script_pylasu_parser import ScriptPylasuParser


class ScriptParserTest(unittest.TestCase):

    def test_pylasu_parse_script(self):
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
