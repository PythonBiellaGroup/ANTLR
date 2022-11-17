from pylasu.support import extension_method
from pylasu.validation import Issue

from interpreter.script_ast import Script
from script_parser.AntlrScriptParser import AntlrScriptParser


@extension_method(AntlrScriptParser.ScriptContext)
def to_ast(self: AntlrScriptParser.ScriptContext, issues: list[Issue]) -> Script:
    raise Exception("")
