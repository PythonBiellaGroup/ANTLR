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
    pass

@dataclass
class Expression(Node):
    pass

@dataclass
class PrintStatement(Statement):
    message: Expression = field(default=None)

@dataclass
class CreateStatement(Statement):
    entity: ReferenceByName = field(default=None)
    name: str = field(default=None)

    def __hash__(self) -> int:
        return self.name.__hash__()


@dataclass
class SetStatement(Statement):
    instance: Expression = field(default=None)
    feature: ReferenceByName = field(default=None)
    value: Expression = field(default=None)

@dataclass
class ReferenceExpression(Expression):
    what: ReferenceByName = field(default=None)
    entity_type: Entity = field(default=None)

@dataclass
class GetInstanceExpression(Expression):
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
