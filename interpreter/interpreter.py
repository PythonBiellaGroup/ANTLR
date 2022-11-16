from typing import Any, List, Optional

from interpreter.entities_ast import Entity, Module, StringType, BooleanType, IntegerType, EntityRefType
from interpreter.controller import Controller


class EntityInstance:
    id: int
    entity: Entity
    values: dict



class Interpreter:
    module: Module
    instances_by_entity: dict
    logs: List[str]

    def __init__(self, module: Module, controller: Controller):
        self.module = module
        self.instances_by_entity = {}
        self.logs = ['Interpreter initialized']
        self.next_id = 1

    def instantiate_entity(self, entity: Entity) -> None:
        new_instance = EntityInstance()
        new_instance.id = self.next_id
        self.next_id = self.next_id + 1
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
        self.logs.append("Added instance of %s: %s" % (entity, new_instance))

    def set_value(self, entity: Entity, feature_name: str, value: Any) -> None:
        pass

    def instances_by_entity_name(self, entity_name):
        e = self.module.get_entity_by_name(entity_name)
        if e not in self.instances_by_entity:
            self.instances_by_entity[e] = []
        return self.instances_by_entity[e]

    def instances_by_id(self, entity_name, instance_id) -> Optional[EntityInstance]:
        e = self.module.get_entity_by_name(entity_name)
        if e not in self.instances_by_entity:
            return None
        matches = [i for i in self.instances_by_entity[e] if i.id == instance_id]
        if len(matches) != 1:
            raise Exception("one instance expected")
        return matches[0]
