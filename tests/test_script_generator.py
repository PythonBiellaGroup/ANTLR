import unittest

from pylasu.model.naming import ReferenceByName

from code_generators import runtime
from code_generators.script import PythonGenerator
from parsers.entities_parser import Module, Entity
from parsers.script_parser import Script, CreateStatement


class ScriptGeneratorTest(unittest.TestCase):

    def simple_module(self) -> Module:
        m = Module()

        client = m.add_entity('Client')
        client.add_str_feature('name')
        client.add_str_feature('address')

        product = m.add_entity('Product')
        product.add_int_feature('value')

        project = m.add_entity('Project')
        project.add_str_feature('name')
        project.add_entity_feature('client', 'Client')

        return m

    def test_creation(self):
        module = self.simple_module()
        generator = PythonGenerator(module)

        script = Script(statements=[
            CreateStatement(
                entity=ReferenceByName[Entity]("Client")
            )
        ])
        issues = []
        cst_module = generator.translate_script(script, issues)
        self.assertEqual(0, len(issues))

        code = cst_module.code
        exec(code, {'instances_by_entity': runtime.instances_by_entity, 'add_entity': runtime.add_entity})

        self.assertEqual(1, len(runtime.instances_by_entity))
