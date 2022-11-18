from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from pylasu.model import Node
from pylasu.model.naming import ReferenceByName


@dataclass
class Module(Node):
    name: str = field(default=None)
    entities: list[Entity] = field(default_factory=list)

    def add_entity(self, name) -> Entity:
        e = Entity()
        e.name = name
        self.entities.append(e)
        return e

    def get_entity_by_name(self, entity_name) -> Entity:
        matches = [e for e in self.entities if e.name == entity_name]
        if len(matches) != 1:
            raise Exception("One entity expected")
        e = matches[0]
        return e


@dataclass
class Entity(Node):
    name: str = field(default=None)
    features: list[Feature] = field(default_factory=list)

    def __hash__(self) -> int:
        return self.name.__hash__()

    def add_str_feature(self, name) -> Feature:
        f = Feature()
        f.name = name
        f.type = StringType()
        self.features.append(f)
        return f

    def add_int_feature(self, name) -> Feature:
        f = Feature()
        f.name = name
        f.type = IntegerType()
        self.features.append(f)
        return f


@dataclass
class Feature(Node):
    name: str = field(default=None)
    type: Type = field(default=None)
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
