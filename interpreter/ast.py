from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from pylasu.model import Node
from pylasu.model.naming import ReferenceByName

@dataclass
class Module(Node):
    entities: list[Entity] = field(default_factory=list)
    observers: list[OnFeatureChange] = field(default_factory=list)

@dataclass
class Entity(Node):
    name: str = field(default=None)
    features: list[Feature] = field(default_factory=list)

    def __hash__(self) -> int:
        return self.name.__hash__()

@dataclass
class Feature(Node):
    name: str = field(default=None)
    type: Type = field(default=None)
    calculated: bool = field(default=False)
    many: bool = field(default=False)

    def __hash__(self) -> int:
        return self.name.__hash__()

@dataclass
class Type(Node):
    pass

@dataclass
class StringType(Type):
    pass

@dataclass
class IntegerType(Type):
    pass

@dataclass
class BooleanType(Type):
    pass

@dataclass
class EntityRefType(Type):
    entity: ReferenceByName = field(default=None)

@dataclass
class OnFeatureChange:
    entity: ReferenceByName = field(default=None)
    feature: ReferenceByName = field(default=None)
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
class ReferenceExpression(Expression):
    what: ReferenceByName = field(default=None)