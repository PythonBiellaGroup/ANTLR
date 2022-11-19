from __future__ import annotations
from dataclasses import dataclass, field
from pylasu.model import Node
from pylasu.model.naming import ReferenceByName

from interpreter.entities_parser.entities_ast import Entity


@dataclass
class Script(Node):
    statements: list[Statement] = field(default_factory=list)


@dataclass
class Statement(Node):
    """
    This is abstract and should not be instantiated.
    """
    pass


@dataclass
class Expression(Node):
    """
    This is abstract and should not be instantiated.
    """
    pass


@dataclass
class PrintStatement(Statement):
    """
    For example, print 1 + 2
    """
    message: Expression = field(default=None)


@dataclass
class CreateStatement(Statement):
    """
    For example, create Project       # name=None
             or, create Project as c  # name=c
    """
    entity: ReferenceByName = field(default=None)
    name: str = field(default=None)

    def __hash__(self) -> int:
        return self.name.__hash__()


@dataclass
class SetStatement(Statement):
    """
    For example, set name of Project #1 to 'Foo'
    """
    instance: Expression = field(default=None)
    feature: ReferenceByName = field(default=None)
    value: Expression = field(default=None)


@dataclass
class ReferenceExpression(Expression):
    what: ReferenceByName = field(default=None)


@dataclass
class GetInstanceExpression(Expression):
    """
    For example, Project #1 or Project #(1+1)
    """
    entity: ReferenceByName = field(default=None)
    id: Expression = field(default=None)


@dataclass
class GetFeatureValueExpression(Expression):
    instance: Expression = field(default=None)
    feature: ReferenceByName = field(default=None)


@dataclass
class StringLiteralExpression(Expression):
    value: str = field(default=None)


@dataclass
class IntLiteralExpression(Expression):
    value: int = field(default=None)


@dataclass
class SumExpression(Expression):
    left: Expression = field(default=None)
    right: Expression = field(default=None)


@dataclass
class SubtractionExpression(Expression):
    left: Expression = field(default=None)
    right: Expression = field(default=None)


@dataclass
class DivisionExpression(Expression):
    left: Expression = field(default=None)
    right: Expression = field(default=None)


@dataclass
class MultiplicationExpression(Expression):
    left: Expression = field(default=None)
    right: Expression = field(default=None)


@dataclass
class ConcatExpression(Expression):
    left: Expression = field(default=None)
    right: Expression = field(default=None)


@dataclass
class ErrorExpression(Expression):
    pass
