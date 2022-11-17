import unittest

#from pylasu.StrumentaLanguageSupport import ReferenceByName
from pylasu.model.naming import ReferenceByName

from interpreter.controller import Controller
from interpreter.entities_parser.entities_ast import Module, Entity
from interpreter.interpreter import Interpreter
from interpreter.script_ast import Script, CreateStatement, StringLiteralExpression, \
    ReferenceExpression, SetStatement, PrintStatement


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
        controller = Controller()
        interpreter = Interpreter(module, controller)

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
        controller = Controller()
        interpreter = Interpreter(module, controller)

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
        controller = Controller()
        interpreter = Interpreter(module, controller)

        self.assertEqual([], interpreter.output)
        script = Script(statements=[
            PrintStatement(
                message=StringLiteralExpression("My beautiful message")
            ),
        ])
        interpreter.run_script(script)
        self.assertEqual(["My beautiful message"], interpreter.output)

    # def test_field_access(self):
    #     module = self.simple_module()
    #     controller = Controller()
    #     interpreter = Interpreter(module, controller)
    #
    #     self.assertEqual([], interpreter.output)
    #     script = Script(statements=[
    #         PrintStatement(
    #             message=StringLiteralExpression("My beautiful message")
    #         ),
    #     ])
    #     interpreter.run_script(script)
    #     self.assertEqual(["My beautiful message"], interpreter.output)

    # def test_complete_example(self):
    #     module = self.simple_module()
    #     controller = Controller()
    #     interpreter = Interpreter(module, controller)
    #
    #     self.assertEqual([], interpreter.output)
    #     script = Script(statements=[
    #         CreateStatement(
    #             entity=ReferenceByName[Entity]("Product"),
    #             name="productA"
    #         ),
    #         SetStatement(
    #             instance=ReferenceExpression(
    #                 what=ReferenceByName("productA")
    #             ),
    #             feature=ReferenceByName("value"),
    #             value=IntLiteralExpression(10000)
    #         ),
    #         CreateStatement(
    #             entity=ReferenceByName[Entity]("Product"),
    #             name="productB"
    #         ),
    #         SetStatement(
    #             instance=ReferenceExpression(
    #                 what=ReferenceByName("productB")
    #             ),
    #             feature=ReferenceByName("value"),
    #             value=IntLiteralExpression(35000)
    #         ),
    #         PrintStatement(
    #             message=ConcatExpression(
    #                 left=StringLiteralExpression("Revenues from A: "),
    #                 right=MultiplicationExpression(
    #                     left=IntLiteralExpression(4),
    #                     right=FieldAccessExpression(
    #                         instance=ReferenceExpression("productA"),
    #                         field=ReferenceByName("value")
    #                 )
    #             )
    #         )),
    #         PrintStatement(
    #             message=ConcatExpression(
    #                 left=StringLiteralExpression("Revenues from B: "),
    #                 right=MultiplicationExpression(
    #                     left=IntLiteralExpression(7),
    #                     right=FieldAccessExpression(
    #                         instance=ReferenceExpression("productB"),
    #                         field=ReferenceByName("value")
    #                     )
    #                 )
    #             ),
    #         ),
    #         PrintStatement(
    #             message=ConcatExpression(
    #                 left=StringLiteralExpression("Total revenues: "),
    #                 right=SumExpression(
    #                     left=MultiplicationExpression(
    #                         left=IntLiteralExpression(7),
    #                         right=FieldAccessExpression(
    #                             instance=ReferenceExpression("productB"),
    #                             field=ReferenceByName("value")
    #                         )
    #                     ),
    #                     right=MultiplicationExpression(
    #                         left=IntLiteralExpression(4),
    #                         right=FieldAccessExpression(
    #                             instance=ReferenceExpression("productA"),
    #                             field=ReferenceByName("value")
    #                         )
    #                     )
    #                 )
    #             ),
    #         )
    #     ])
    #     interpreter.run_script(script)
    #     self.assertEqual([
    #         "Revenues from A: 40,000",
    #         "Revenues from B: 245,000"
    #         "Total revenues: 295,000"], interpreter.output)

