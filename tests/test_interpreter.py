import unittest

from antlr4 import CommonTokenStream, InputStream
#from pylasu.StrumentaLanguageSupport import ReferenceByName
from pylasu.model.naming import ReferenceByName

from interpreter.controller import Controller
from interpreter.entities_ast import Module, Entity, Feature, StringType, IntegerType, EntityRefType
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


    # def test_instance_has_default_values(self):
    #     m = Module()
    #
    #     invoice = Entity()
    #     invoice.name = "Invoice"
    #
    #     invoice_number = Feature()
    #     invoice_number.name = "number"
    #     invoice_number.type = IntegerType()
    #     invoice.features.append(invoice_number)
    #
    #     invoice_total = Feature()
    #     invoice_total.name = "total"
    #     invoice_total.type = IntegerType()
    #     invoice_total.calculated = True
    #     invoice.features.append(invoice_total)
    #
    #     invoice_number_of_lines = Feature()
    #     invoice_number_of_lines.name = "number_of_lines"
    #     invoice_number_of_lines.type = IntegerType()
    #     invoice_number_of_lines.calculated = True
    #     invoice.features.append(invoice_number_of_lines)
    #
    #     invoice_lines = Feature()
    #     invoice_lines.name = "lines"
    #     invoice_lines.type = EntityRefType()
    #     invoice_lines.type.entity = ReferenceByName(name="InvoiceLine")
    #     invoice_lines.many = True
    #     invoice.features.append(invoice_lines)
    #
    #     m.entities.append(invoice)
    #
    #     invoice_line = Entity()
    #     invoice_line.name = "InvoiceLine"
    #
    #     invoice_line_description = Feature()
    #     invoice_line_description.name = "description"
    #     invoice_line_description.type = StringType()
    #     invoice_line.features.append(invoice_line_description)
    #
    #     invoice_line_value = Feature()
    #     invoice_line_value.name = "value"
    #     invoice_line_value.type = IntegerType()
    #     invoice_line.features.append(invoice_line_value)
    #
    #     m.entities.append(invoice_line)
    #
    #     controller = DummyController()
    #     interpreter = Interpreter(m, controller)
    #
    #     interpreter.instantiate_entity(invoice)
    #     self.assertEqual(1, len(interpreter.instances_by_entity[invoice]))
    #     invoice_1 = interpreter.instances_by_entity[invoice][0]
    #     self.assertEqual(0, invoice_1.values[invoice_number])
    #     self.assertEqual(0, invoice_1.values[invoice_total])
    #     self.assertEqual([], invoice_1.values[invoice_lines])
    #     self.assertEqual(0, invoice_1.values[invoice_number_of_lines])
