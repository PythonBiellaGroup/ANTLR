from dataclasses import dataclass
from typing import List, Optional

from pylasu.model import Node
from pylasu.validation import Issue, IssueType

from parsers.entities_parser import Type, StringType, IntegerType, EntityRefType, Entity, Feature
from parsers.script_parser import Script, ReferenceExpression, GetInstanceExpression, GetFeatureValueExpression, \
    StringLiteralExpression, IntLiteralExpression, DivisionExpression


@dataclass
class RType(Node):
    def can_be_assigned(self, other_type: 'RType') -> bool:
        return self == other_type

    @classmethod
    def from_type(cls, type: Type):
        if isinstance(type, StringType):
            return RStringType()
        elif isinstance(type, IntegerType):
            return RIntegerType()
        elif isinstance(type, EntityRefType):
            assert type.entity.resolved()
            return REntityRefType(type.entity.referred)
        else:
            raise Exception("%s is not supported" % str(type))


@dataclass
class RStringType(RType):
    pass


@dataclass
class RIntegerType(RType):
    pass


@dataclass
class RBooleanType(RType):
    pass


@dataclass
class REntityRefType(RType):
    entity: Entity

    def __post_init__(self):
        if self.entity is None:
            raise Exception("Unresolved")


def to_runtime_type(type) -> RType:
    if isinstance(type, EntityRefType):
        if not type.entity.resolved():
            raise Exception("Cannot translate unresolved entity reference to %s" % type.entity.name)
        return REntityRefType(entity=type.entity.referred)
    raise Exception("unsupported %s" % str(type))


def compute_type(script: Script, node: Node, issues: List[Issue]) -> Optional[RType]:
    if isinstance(node, ReferenceExpression):
        if not node.what.referred.entity.resolved():
            issues.append(Issue(type=IssueType.SEMANTIC,
                                position=node.position,
                                message="Entity cannot be resolved: %s" % str(node.what.referred.entity.name)))
            return None
        return REntityRefType(node.what.referred.entity.referred)
    elif isinstance(node, GetInstanceExpression):
        return REntityRefType(node.entity.referred)
    elif isinstance(node, GetFeatureValueExpression):
        instance_type = compute_type(script, node.instance, issues)
        if not isinstance(instance_type, REntityRefType):
            issues.append(Issue(type=IssueType.SEMANTIC,
                                position=node.position,
                                message="Instance has not entity type but type %s" % str(instance_type)))
            return None
        resolved = node.feature.try_to_resolve(instance_type.entity.features)
        if not resolved:
            issues.append(Issue(type=IssueType.SEMANTIC,
                                position=node.position,
                                message="Feature %s not found in entity %s" % (
                                    node.feature.name, str(instance_type.entity))))
            return None
        return to_runtime_type(node.feature.referred.type)
    elif isinstance(node, Feature):
        return RType.from_type(node.type)
    elif isinstance(node, StringLiteralExpression):
        return RStringType()
    elif isinstance(node, IntLiteralExpression):
        return RIntegerType()
    elif isinstance(node, DivisionExpression):
        return RIntegerType()
    else:
        raise Exception("Unable to calculate type for %s" % (str(node)))
