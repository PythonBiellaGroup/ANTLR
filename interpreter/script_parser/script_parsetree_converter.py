from pylasu.model.naming import ReferenceByName
from pylasu.parsing.parse_tree import ParseTreeOrigin
from pylasu.support import extension_method
from pylasu.validation import Issue

from interpreter.script_parser.script_ast import Script, CreateStatement, ReferenceExpression, StringLiteralExpression, \
    SetStatement, DivisionExpression, MultiplicationExpression, SumExpression, SubtractionExpression, Expression, \
    IntLiteralExpression, PrintStatement, ConcatExpression, GetFeatureValueExpression, ErrorExpression, \
    GetInstanceExpression
from script_parser.AntlrScriptParser import AntlrScriptParser


@extension_method(AntlrScriptParser.ScriptContext)
def to_ast(self: AntlrScriptParser.ScriptContext, issues: list[Issue]) -> Script:
    return Script(statements=[c.to_ast(issues) for c in self.statements]).with_origin(ParseTreeOrigin(self))


@extension_method(AntlrScriptParser.Create_statementContext)
def to_ast(self: AntlrScriptParser.Create_statementContext, issues: list[Issue]) -> CreateStatement:
    return CreateStatement(
        entity=ReferenceByName(name=self.entity.text),
        name=self.var_name.text if self.var_name is not None else None
    ).with_origin(ParseTreeOrigin(self))


@extension_method(AntlrScriptParser.Set_statementContext)
def to_ast(self: AntlrScriptParser.Set_statementContext, issues: list[Issue]) -> SetStatement:
    return SetStatement(
        instance=self.instance.to_ast(issues),
        feature=ReferenceByName(name=self.feature.text),
        value=self.value.to_ast(issues)
    ).with_origin(ParseTreeOrigin(self))


@extension_method(AntlrScriptParser.Print_statementContext)
def to_ast(self: AntlrScriptParser.Print_statementContext, issues: list[Issue]) -> PrintStatement:
    return PrintStatement(
        message=self.message.to_ast(issues)
    ).with_origin(ParseTreeOrigin(self))


@extension_method(AntlrScriptParser.Reference_expressionContext)
def to_ast(self: AntlrScriptParser.Reference_expressionContext, issues: list[Issue]) -> ReferenceExpression:
    return ReferenceExpression(what=ReferenceByName(name=self.name.text)).with_origin(ParseTreeOrigin(self))


@extension_method(AntlrScriptParser.String_literal_expressionContext)
def to_ast(self: AntlrScriptParser.String_literal_expressionContext, issues: list[Issue]) -> StringLiteralExpression:
    return StringLiteralExpression(value=self.STR_VALUE().symbol.text[1:-1]).with_origin(ParseTreeOrigin(self))


@extension_method(AntlrScriptParser.Int_literal_expressionContext)
def to_ast(self: AntlrScriptParser.Int_literal_expressionContext, issues: list[Issue]) -> IntLiteralExpression:
    return IntLiteralExpression(value=int(self.INT_VALUE().symbol.text)).with_origin(ParseTreeOrigin(self))


@extension_method(AntlrScriptParser.Div_mult_expressionContext)
def to_ast(self: AntlrScriptParser.Div_mult_expressionContext, issues: list[Issue]) -> Expression:
    if self.op.text == '/':
        return DivisionExpression(left=self.left.to_ast(issues), right=self.right.to_ast(issues)).with_origin(ParseTreeOrigin(self))
    elif self.op.text == '*':
        return MultiplicationExpression(left=self.left.to_ast(issues), right=self.right.to_ast(issues)).with_origin(ParseTreeOrigin(self))
    else:
        raise Exception("Unexpected operator")


@extension_method(AntlrScriptParser.Sum_sub_expressionContext)
def to_ast(self: AntlrScriptParser.Sum_sub_expressionContext, issues: list[Issue]) -> Expression:
    if self.op.text == '+':
        return SumExpression(left=self.left.to_ast(issues), right=self.right.to_ast(issues)).with_origin(ParseTreeOrigin(self))
    elif self.op.text == '-':
        return SubtractionExpression(left=self.left.to_ast(issues), right=self.right.to_ast(issues)).with_origin(ParseTreeOrigin(self))
    else:
        raise Exception("Unexpected operator")


@extension_method(AntlrScriptParser.Parens_expressionContext)
def to_ast(self: AntlrScriptParser.Parens_expressionContext, issues: list[Issue]) -> Expression:
    return self.expression().to_ast(issues)


@extension_method(AntlrScriptParser.Concat_expressionContext)
def to_ast(self: AntlrScriptParser.Concat_expressionContext, issues: list[Issue]) -> Expression:
    try:
        return ConcatExpression(left=self.left.to_ast(issues), right=self.right.to_ast(issues)).with_origin(ParseTreeOrigin(self))
    except:
        return ErrorExpression()


@extension_method(AntlrScriptParser.Feature_access_expressionContext)
def to_ast(self: AntlrScriptParser.Feature_access_expressionContext, issues: list[Issue]) -> GetFeatureValueExpression:
    return GetFeatureValueExpression(instance=self.instance.to_ast(issues),
                                     feature=ReferenceByName(name=self.feature.text)).with_origin(ParseTreeOrigin(self))


@extension_method(AntlrScriptParser.Entity_by_id_expressionContext)
def to_ast(self: AntlrScriptParser.Entity_by_id_expressionContext, issues: list[Issue]) -> GetInstanceExpression:
    return GetInstanceExpression(id=self.id_.to_ast(issues),
                                 entity=ReferenceByName(name=self.entity.text)).with_origin(ParseTreeOrigin(self))
