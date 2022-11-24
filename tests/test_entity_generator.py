import unittest

from pylasu.model.naming import ReferenceByName

from parsers.entities_parser import Module, Entity, Feature, StringType, IntegerType, EntityRefType
import code_generators.entities


class EntityGeneratorTest(unittest.TestCase):
    def test_empty_module_generator(self):
        self.assertEqual("", Module().to_python())

    def test_module_generator(self):
        person = Entity(name='Person',
                        features=[
                            Feature(name='name', type=StringType()),
                            Feature(name='address', type=StringType()),
                        ])
        vehicle = Entity(name='Vehicle',
                         features=[
                             Feature(name='license_plate', type=StringType()),
                             Feature(name='year', type=IntegerType()),
                             Feature(name='owner', type=EntityRefType(entity=ReferenceByName(name='Person'))),
                         ])
        module = Module(name='Insurance', entities=[person, vehicle])
        self.assertEqual('''from dataclasses import dataclass

@dataclass
class Person:
    name: str
    address: str


@dataclass
class Vehicle:
    license_plate: str
    year: int
    owner: "Person"

''', module.to_python())
