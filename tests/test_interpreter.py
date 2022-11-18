import unittest

from pylasu.model.naming import ReferenceByName

from interpreter.entities_parser.entities_ast import Module, Entity
from interpreter.interpreter import Interpreter
from interpreter.script_parser.script_ast import Script, CreateStatement, StringLiteralExpression, \
    ReferenceExpression, SetStatement, PrintStatement
from interpreter.script_parser.script_pylasu_parser import ScriptPylasuParser


class DummyController(object):
    pass


class InterpreterTest(unittest.TestCase):

    def simple_module(self) -> Module:
        m = Module()
        client = m.add_entity('Client')
        client.add_str_feature('name')
        client.add_str_feature('address')
        product = m.add_entity('Product')
        product.add_int_feature('value')
        project = m.add_entity('Project')
        return m

    def test_creation(self):
        module = self.simple_module()
        interpreter = Interpreter(module)

        self.assertEqual(0, len(interpreter.instances_by_entity_name('Client')))
        self.assertEqual(0, len(interpreter.instances_by_entity_name('Product')))
        self.assertEqual(0, len(interpreter.instances_by_entity_name('Project')))

        script = Script(statements=[
            CreateStatement(
                entity=ReferenceByName[Entity]("Client")
            )
        ])
        interpreter.run_script(script)

        self.assertEqual(1, len(interpreter.instances_by_entity_name('Client')))
        self.assertEqual(0, len(interpreter.instances_by_entity_name('Product')))
        self.assertEqual(0, len(interpreter.instances_by_entity_name('Project')))

        c1 = interpreter.instances_by_entity_name('Client')[0]
        self.assertEqual(1, c1.id)
        self.assertEqual("<unspecified>", c1['name'])
        self.assertEqual("<unspecified>", c1['address'])

    def test_set_statement(self):
        module = self.simple_module()
        interpreter = Interpreter(module)

        self.assertEqual(0, len(interpreter.instances_by_entity_name('Client')))
        self.assertEqual(0, len(interpreter.instances_by_entity_name('Product')))
        self.assertEqual(0, len(interpreter.instances_by_entity_name('Project')))

        script = Script(statements=[
            CreateStatement(
                entity=ReferenceByName[Entity]("Client"),
                name="newClient"
            ),
            SetStatement(
                instance=ReferenceExpression(
                    what=ReferenceByName("newClient")
                ),
                feature=ReferenceByName("name"),
                value=StringLiteralExpression("Acme Inc.")
            )
        ])
        interpreter.run_script(script)

        self.assertEqual(1, len(interpreter.instances_by_entity_name('Client')))
        self.assertEqual(0, len(interpreter.instances_by_entity_name('Product')))
        self.assertEqual(0, len(interpreter.instances_by_entity_name('Project')))

        c1 = interpreter.instances_by_entity_name('Client')[0]
        self.assertEqual(1, c1.id)
        self.assertEqual("Acme Inc.", c1['name'])
        self.assertEqual("<unspecified>", c1['address'])

    def test_print_statement(self):
        module = self.simple_module()
        interpreter = Interpreter(module, verbose=False)

        self.assertEqual([], interpreter.output)
        script = Script(statements=[
            PrintStatement(
                message=StringLiteralExpression("My beautiful message")
            ),
        ])
        interpreter.run_script(script)
        self.assertEqual(["My beautiful message"], interpreter.output)

    def test_access_expression(self):
        module = self.simple_module()
        interpreter = Interpreter(module, verbose=False)

        script_code = '''
        create Client
        set name of Client #1 to 'ACME Inc.'
        create Product
        set value of Product #2 to (1500 + 200) / 2
        print concat 'Value of Product #2 is: ' and value of Product #2
        '''
        self.assertEqual([], interpreter.output)
        result = ScriptPylasuParser().parse(script_code)
        self.assertEqual([], result.issues)
        interpreter.run_script(result.root)
        self.assertEqual(["Value of Product #2 is: 850"], interpreter.output)


