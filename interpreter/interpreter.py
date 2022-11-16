from typing import Any, List, Optional, Iterable

from interpreter.entities_ast import Entity, Module, StringType, BooleanType, IntegerType, EntityRefType
from interpreter.controller import Controller
from interpreter.script_ast import CreateStatement, Script, SetStatement, ReferenceExpression, StringLiteralExpression


class EntityInstance:
    id: int
    entity: Entity
    values: dict

    def __getitem__(self, name: str) -> Any:
        for k in self.values.keys():
            if k.name == name:
                return self.values[k]
        raise Exception("Unknown feature %s" % name)

    def set_feature(self, feature, value):
        self.values[feature] = value


class Interpreter:
    module: Module
    instances_by_entity: dict
    logs: List[str]

    def __init__(self, module: Module, controller: Controller):
        self.module = module
        self.instances_by_entity = {}
        self.logs = ['Interpreter initialized']
        self.next_id = 1

    def __instantiate_entity__(self, entity: Entity) -> None:
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
            new_instance.set_feature(feature, feature_value)
        if entity not in self.instances_by_entity:
            self.instances_by_entity[entity] = []
        self.instances_by_entity[entity].append(new_instance)
        self.logs.append("Added instance of %s: %s" % (entity, new_instance))
        return new_instance

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

    def __resolve__(self, script: Script):
        for s in script.walk_descendants(restrict_to=CreateStatement):
            s.entity.try_to_resolve(self.module.entities)
        for e in script.walk_descendants(restrict_to=ReferenceExpression):
            e.what.try_to_resolve(script.walk_descendants(restrict_to=CreateStatement))
            e.entity_type = e.what.referred.entity.referred
        for s in script.walk_descendants(restrict_to=SetStatement):
            if s.instance is None:
                raise Exception("We did not expected s.instance to be null for %s" % str(s.instance))
            entity = s.instance.entity_type
            if entity is None:
                raise Exception("We did not expected entity to be null for %s" % str(s))
            s.feature.try_to_resolve(entity.features)
            if not s.feature.resolved():
                raise Exception("Unable to resolve feature reference in %s. Candidates: %s" % (str(s), str(entity.features)))

    def run_script(self, script):
        self.__resolve__(script)
        symbol_table = {}
        for s in script.statements:
            self.execute_statement(s, symbol_table)

    def evaluate_expression(self, expression, symbol_table) -> Any:
        if isinstance(expression, ReferenceExpression):
            if expression.what.referred is None:
                raise Exception("Unresolved expression %s" % str(expression))
            if expression.what.referred not in symbol_table:
                raise Exception("I cannot find %s in symbol table %s" % (str(expression.what.referred), str(symbol_table)))
            return symbol_table[expression.what.referred]
        elif isinstance(expression, StringLiteralExpression):
            return expression.value
        else:
            raise Exception("Unable to evaluate expression %s" % str(expression))

    def execute_statement(self, statement, symbol_table):
        if isinstance(statement, CreateStatement):
            instance = self.__instantiate_entity__(statement.entity.referred)
            if statement.name is not None:
                symbol_table[statement] = instance
        elif isinstance(statement, SetStatement):
            instance = self.evaluate_expression(statement.instance, symbol_table)
            value = self.evaluate_expression(statement.value, symbol_table)
            instance.set_feature(statement.feature.referred, value)
        else:
            raise Exception("Unable to execute statement %s" % str(statement))
