from typing import List

import libcst
from libcst import Comment, EmptyLine
from pylasu.validation import Issue, IssueType

import code_generators.entities
from parsers.entities_parser import Module
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
        result = libcst.parse_module(f'''{self.module.to_python()}

''')
        for s in script.statements:
            # Nota: i nodi di Libcst sono immutabili
            result = self.translate_statement(s, result, issues)
        return result

    def translate_statement(self, statement: Statement, module: libcst.Module, issues: List[Issue]):
        if isinstance(statement, CreateStatement):
            if statement.entity.resolved():
                code = f"add_entity({statement.entity.referred.name}, {statement.entity.referred.name}())"
                if statement.name:
                    code = f"{statement.name} = " + code
                stmts = libcst.parse_module(code)
                return module.with_changes(body=module.body + stmts.body)
            else:
                message = "Cannot instantiate entity named %s" % statement.entity.name
                issues.append(Issue(type=IssueType.SEMANTIC,
                                    position=statement.position,
                                    message=message))
                return module.with_changes(body=module.body + [EmptyLine(comment=Comment(f"# {message}"))])
        else:
            return module

    def clear_logs(self):
        self.output = []
