from typing import Any, List, Optional

from pylasu.validation import Issue, IssueType

from parsers.entities_parser.entities_ast import Entity, Module, StringType, BooleanType, IntegerType, \
    EntityRefType
from parsers.script_parser import CreateStatement, SetStatement, ReferenceExpression, \
    StringLiteralExpression, \
    PrintStatement, GetInstanceExpression, IntLiteralExpression, DivisionExpression, SumExpression, ConcatExpression, \
    GetFeatureValueExpression, MultiplicationExpression
from support.resolution import resolve_module, resolve_script


class EntityInstance:
    id: int
    entity: Entity
    values: dict

    def __str__(self) -> str:
        for k in self.values.keys():
            if k.name == 'name':
                return str(self.values[k])
        return "%s(id=%s,value=%s)" % (self.entity.name, str(self.id), str(self.values))

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
    output: List[str]

    def __init__(self, module: Module, verbose: bool = True):
        self.module = module
        issues = []
        resolve_module(self.module, issues)
        if len(issues) > 0:
            raise Exception("Issues in nodule: %s" % str(issues))

        self.instances_by_entity = {}
        self.next_id = 1
        self.verbose = verbose
        if self.verbose:
            self.output = ['Interpreter initialized']
        else:
            self.output = []

    def instantiate_entity(self, entity: Entity) -> EntityInstance:
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
        if self.verbose:
            self.output.append("Added instance of %s: %s" % (entity, new_instance))
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

    def run_script(self, script) -> List[Issue]:
        issues = []
        resolve_script(self.module, script, issues)
        symbol_table = {}
        for s in script.statements:
            self.execute_statement(s, symbol_table, issues)
        return issues

    def evaluate_expression(self, expression, symbol_table, issues: List[Issue]) -> Any:
        if isinstance(expression, ReferenceExpression):
            if expression.what.referred is None:
                raise Exception("Unresolved expression %s" % str(expression))
            if expression.what.referred not in symbol_table:
                raise Exception(
                    "I cannot find %s in symbol table %s" % (str(expression.what.referred), str(symbol_table)))
            return symbol_table[expression.what.referred]
        elif isinstance(expression, StringLiteralExpression):
            return expression.value
        elif isinstance(expression, IntLiteralExpression):
            return expression.value
        elif isinstance(expression, DivisionExpression):
            left = self.evaluate_expression(expression.left, symbol_table, issues)
            right = self.evaluate_expression(expression.right, symbol_table, issues)
            return int(left / right)
        elif isinstance(expression, MultiplicationExpression):
            left = self.evaluate_expression(expression.left, symbol_table, issues)
            right = self.evaluate_expression(expression.right, symbol_table, issues)
            return left * right
        elif isinstance(expression, SumExpression):
            left = self.evaluate_expression(expression.left, symbol_table, issues)
            right = self.evaluate_expression(expression.right, symbol_table, issues)
            return left + right
        elif isinstance(expression, ConcatExpression):
            left = self.evaluate_expression(expression.left, symbol_table, issues)
            right = self.evaluate_expression(expression.right, symbol_table, issues)
            return str(left) + str(right)
        elif isinstance(expression, GetInstanceExpression):
            id = self.evaluate_expression(expression.id, symbol_table, issues)
            if expression.entity.referred not in self.instances_by_entity:
                issues.append(Issue(type=IssueType.SEMANTIC,
                                    position=expression.position,
                                    message="Unable to find instance of %s with id %s" % (
                                        expression.entity.name, str(id))))
                return None
            instances = self.instances_by_entity[expression.entity.referred]
            matching = [i for i in instances if i.id == id]
            if len(matching) != 1:
                issues.append(Issue(type=IssueType.SEMANTIC,
                                    position=expression.position,
                                    message="Unable to find instance of %s with id %s" % (
                                        expression.entity.name, str(id))))
                return None
            return matching[0]
        elif isinstance(expression, GetFeatureValueExpression):
            instance = self.evaluate_expression(expression.instance, symbol_table, issues)
            if instance is None:
                issues.append(Issue(type=IssueType.SEMANTIC,
                                    position=expression.position,
                                    message="Cannot evaluate access to feature %s as the instance cannot be calculated" % expression.feature.name))
                return None
            value = instance.values[expression.feature.referred]
            if value is None:
                issues.append(Issue(type=IssueType.SEMANTIC,
                                    position=expression.position,
                                    message="Feature %s not found in %s" % (expression.feature.name, str(instance))))
                return None
            return value
        else:
            raise Exception("Unable to evaluate expression %s" % str(expression))

    def execute_statement(self, statement, symbol_table, issues: List[Issue]):
        if isinstance(statement, CreateStatement):
            if not statement.entity.resolved():
                issues.append(Issue(type=IssueType.SEMANTIC,
                                    position=statement.position,
                                    message="Cannot instantiate entity named %s" % statement.entity.name))
                return
            instance = self.instantiate_entity(statement.entity.referred)
            if statement.name is not None:
                symbol_table[statement] = instance
        elif isinstance(statement, SetStatement):
            instance = self.evaluate_expression(statement.instance, symbol_table, issues)
            value = self.evaluate_expression(statement.value, symbol_table, issues)
            instance.set_feature(statement.feature.referred, value)
        elif isinstance(statement, PrintStatement):
            message = self.evaluate_expression(statement.message, symbol_table, issues)
            if message is not None:
                self.output.append(str(message))
        else:
            raise Exception("Unable to execute statement %s" % str(statement))

    def clear_logs(self):
        self.output = []
