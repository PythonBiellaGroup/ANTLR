from pylasu.model.naming import ReferenceByName
from pylasu.support import extension_method
from pylasu.validation import Issue

from interpreter.script_parser.script_ast import Script, CreateStatement, ReferenceExpression, StringLiteralExpression, \
    SetStatement, DivisionExpression, MultiplicationExpression, SumExpression, SubtractionExpression
from script_parser.AntlrScriptParser import AntlrScriptParser


@extension_method(AntlrScriptParser.ScriptContext)
def to_ast(self: AntlrScriptParser.ScriptContext, issues: list[Issue]) -> Script:
    return Script(statements=[c.to_ast(issues) for c in self.statements])


@extension_method(AntlrScriptParser.Create_statementContext)
def to_ast(self: AntlrScriptParser.Create_statementContext, issues: list[Issue]) -> Script:
    return CreateStatement(
        entity=ReferenceByName(name=self.entity.text),
        name=self.var_name.text
    )


@extension_method(AntlrScriptParser.Set_statementContext)
def to_ast(self: AntlrScriptParser.Set_statementContext, issues: list[Issue]) -> Script:
    return SetStatement(
        instance=self.instance.to_ast(issues),
        feature=ReferenceByName(name=self.feature.text),
        value=self.value.to_ast(issues)
    )


@extension_method(AntlrScriptParser.Reference_expressionContext)
def to_ast(self: AntlrScriptParser.Reference_expressionContext, issues: list[Issue]) -> Script:
    return ReferenceExpression(what=ReferenceByName(name=self.name.text))


@extension_method(AntlrScriptParser.String_literal_expressionContext)
def to_ast(self: AntlrScriptParser.String_literal_expressionContext, issues: list[Issue]) -> Script:
    return StringLiteralExpression(value=self.STR_VALUE().symbol.text)


@extension_method(AntlrScriptParser.Int_literal_expressionContext)
def to_ast(self: AntlrScriptParser.Int_literal_expressionContext, issues: list[Issue]) -> Script:
    return StringLiteralExpression(value=int(self.INT_VALUE().symbol.text))


@extension_method(AntlrScriptParser.Div_mult_expressionContext)
def to_ast(self: AntlrScriptParser.Div_mult_expressionContext, issues: list[Issue]) -> Script:
    if self.op.text == '/':
        return DivisionExpression(left=self.left.to_ast(issues), right=self.right.to_ast(issues))
    elif self.op.text == '*':
        return MultiplicationExpression(left=self.left.to_ast(issues), right=self.right.to_ast(issues))
    else:
        raise Exception("Unexpected operator")


@extension_method(AntlrScriptParser.Sum_sub_expressionContext)
def to_ast(self: AntlrScriptParser.Sum_sub_expressionContext, issues: list[Issue]) -> Script:
    if self.op.text == '+':
        return SumExpression(left=self.left.to_ast(issues), right=self.right.to_ast(issues))
    elif self.op.text == '-':
        return SubtractionExpression(left=self.left.to_ast(issues), right=self.right.to_ast(issues))
    else:
        raise Exception("Unexpected operator")


@extension_method(AntlrScriptParser.Parens_expressionContext)
def to_ast(self: AntlrScriptParser.Parens_expressionContext, issues: list[Issue]) -> Script:
    return self.expression().to_ast(issues)