from typing import List, Optional

import libcst
from libcst import Arg, Comment, EmptyLine, Expr, Name, SimpleStatementLine
from pylasu.validation import Issue, IssueType

import code_generators.entities
from parsers.entities_parser import Module, Entity, StringType, BooleanType, IntegerType, EntityRefType
from parsers.script_parser import CreateStatement, Statement
from support.resolution import resolve_module, resolve_script


class PythonGenerator:
    module: Module
    output: List[str]
    verbose: bool

    def __init__(self, module: Module, verbose: bool = True):
        self.module = module
        issues = []
        resolve_module(self.module, issues)
        if len(issues) > 0:
            raise Exception("Issues in nodule: %s" % str(issues))

        self.verbose = verbose
        if self.verbose:
            self.output = ['Generator initialized']
        else:
            self.output = []

    def translate_script(self, script, issues: List[Issue]) -> libcst.Module:
        resolve_script(self.module, script, issues)
        entities_setup_code = f'{self.module.to_python()}'
        result = libcst.parse_module(entities_setup_code)
        for s in script.statements:
            # Nota: i nodi di Libcst sono immutabili
            result = self.translate_statement(s, result, issues)
        return result

    def translate_statement(self, statement: Statement, module: libcst.Module, issues: List[Issue]):
        if isinstance(statement, CreateStatement):
            if statement.entity.resolved():
                entity = statement.entity.referred
                name = statement.name
                stmts = instantiate_entity(entity, name)
                return module.with_changes(body=module.body + [EmptyLine(), EmptyLine()] + stmts, footer=[])
            else:
                message = "Cannot instantiate entity named %s" % statement.entity.name
                return report_issue(message, module, statement, issues)
        else:
            message = f"I don't know how to translate a node of type {type(statement).__name__} yet."
            return report_issue(message, module, statement, issues)

    def clear_logs(self):
        self.output = []


def report_issue(message, module, node, issues):
    issues.append(Issue(type=IssueType.SEMANTIC, position=node.position, message=message))
    return module.with_changes(body=module.body + [EmptyLine(comment=Comment(f"# {message}"))])


def instantiate_entity(entity: Entity, name: Optional[str]):
    code = f"add_entity({entity.name})"
    expr = libcst.parse_expression(code)
    for feature in entity.features:
        if feature.many:
            feature_value = "[]"
        elif isinstance(feature.type, StringType):
            feature_value = "'<unspecified>'"
        elif isinstance(feature.type, BooleanType):
            feature_value = "False"
        elif isinstance(feature.type, IntegerType):
            feature_value = "0"
        elif isinstance(feature.type, EntityRefType):
            feature_value = None
        else:
            raise Exception("Unsupported type %s (feature: %s)" % (str(feature.type), str(feature)))
        if feature_value is not None:
            expr = expr.with_changes(
                args=expr.args + (Arg(keyword=Name(feature.name), value=libcst.parse_expression(feature_value)),))
    if name:
        stmt = libcst.parse_statement(f'{name} = e')
        stmt = stmt.with_deep_changes(stmt.body[0], value=expr)
    else:
        stmt = SimpleStatementLine(body=[Expr(value=expr)])
    return [stmt]
