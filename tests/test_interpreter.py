import unittest

from antlr4 import CommonTokenStream, InputStream
from pylasu.StrumentaLanguageSupport import ReferenceByName

from interpreter.entities_ast import Module, Entity, Feature, StringType, IntegerType, EntityRefType
from interpreter.interpreter import Interpreter


class DummyController(object):
    pass


class InterpreterTest(unittest.TestCase):

    def test_instance_has_default_values(self):
        m = Module()

        invoice = Entity()
        invoice.name = "Invoice"

        invoice_number = Feature()
        invoice_number.name = "number"
        invoice_number.type = IntegerType()
        invoice.features.append(invoice_number)

        invoice_total = Feature()
        invoice_total.name = "total"
        invoice_total.type = IntegerType()
        invoice_total.calculated = True
        invoice.features.append(invoice_total)

        invoice_number_of_lines = Feature()
        invoice_number_of_lines.name = "number_of_lines"
        invoice_number_of_lines.type = IntegerType()
        invoice_number_of_lines.calculated = True
        invoice.features.append(invoice_number_of_lines)

        invoice_lines = Feature()
        invoice_lines.name = "lines"
        invoice_lines.type = EntityRefType()
        invoice_lines.type.entity = ReferenceByName(name="InvoiceLine")
        invoice_lines.many = True
        invoice.features.append(invoice_lines)

        m.entities.append(invoice)

        invoice_line = Entity()
        invoice_line.name = "InvoiceLine"

        invoice_line_description = Feature()
        invoice_line_description.name = "description"
        invoice_line_description.type = StringType()
        invoice_line.features.append(invoice_line_description)

        invoice_line_value = Feature()
        invoice_line_value.name = "value"
        invoice_line_value.type = IntegerType()
        invoice_line.features.append(invoice_line_value)

        m.entities.append(invoice_line)

        controller = DummyController()
        interpreter = Interpreter(m, controller)

        interpreter.instantiate_entity(invoice)
        self.assertEqual(1, len(interpreter.instances_by_entity[invoice]))
        invoice_1 = interpreter.instances_by_entity[invoice][0]
        self.assertEqual(0, invoice_1.values[invoice_number])
        self.assertEqual(0, invoice_1.values[invoice_total])
        self.assertEqual([], invoice_1.values[invoice_lines])
        self.assertEqual(0, invoice_1.values[invoice_number_of_lines])
