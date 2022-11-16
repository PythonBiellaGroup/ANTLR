from typing import Any, List

from interpreter.entities_ast import Entity, Module, StringType, BooleanType, IntegerType, EntityRefType
from interpreter.controller import Controller


class EntityInstance:
    entity: Entity
    values: dict



class Interpreter:
    module: Module
    instances_by_entity: dict

    def __init__(self, module: Module, controller: Controller):
        self.module = module
        self.instances_by_entity = {}

    def instantiate_entity(self, entity: Entity) -> None:
        new_instance = EntityInstance
        new_instance.entity = entity
        new_instance.values = {}
        for feature in entity.features:
            if feature.many:
                feature_value = []
            elif isinstance(feature.type, StringType):
                feature_value = "<unspecified>"
            elif isinstance(feature.type, BooleanType):
                feature_value = False
            elif isinstance(feature.type, IntegerType):
                feature_value = 0
            elif isinstance(feature.type, EntityRefType):
                feature_value = None
            else:
                raise Exception("Unsupported type %s (feature: %s)" % (str(feature.type), str(feature)))
            new_instance.values[feature] = feature_value
        if entity not in self.instances_by_entity:
            self.instances_by_entity[entity] = []
        self.instances_by_entity[entity].append(new_instance)

    def set_value(self, entity: Entity, feature_name: str, value: Any) -> None:
        pass

    def instances_by_entity_name(self, entity_name):
        e = self.module.get_entity_by_name(entity_name)
        if e not in self.instances_by_entity:
            self.instances_by_entity[e] = []
        return self.instances_by_entity[e]
