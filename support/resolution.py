from typing import List

from pylasu.validation import Issue, IssueType

from parsers.entities_parser import Module, EntityRefType
from parsers.script_parser import Script, GetInstanceExpression, CreateStatement, ReferenceExpression, SetStatement, \
    GetFeatureValueExpression
from support.types import compute_type, REntityRefType


def resolve_module(module: Module, issues: List[Issue]):
    for t in module.walk_descendants(restrict_to=EntityRefType):
        resolved = t.entity.try_to_resolve(module.entities)
        if not resolved:
            issues.append(Issue(type=IssueType.SEMANTIC,
                                position=t.position,
                                message="Cannot find entity named %s" % t.entity.name))


def resolve_script(module: Module, script: Script, issues: List[Issue]):
    for t in script.walk_descendants(restrict_to=EntityRefType):
        resolved = t.entity.try_to_resolve(module.entities)
        if not resolved:
            issues.append(Issue(type=IssueType.SEMANTIC,
                                position=t.position,
                                message="Cannot find entity named %s" % t.entity.name))
    for s in script.walk_descendants(restrict_to=GetInstanceExpression):
        s.entity.try_to_resolve(module.entities)
    for s in script.walk_descendants(restrict_to=CreateStatement):
        resolved = s.entity.try_to_resolve(module.entities)
        if not resolved:
            issues.append(Issue(type=IssueType.SEMANTIC,
                                position=s.position,
                                message="Cannot find entity named %s" % s.entity.name))
    for e in script.walk_descendants(restrict_to=ReferenceExpression):
        resolved = e.what.try_to_resolve(script.walk_descendants(restrict_to=CreateStatement))
        if not resolved:
            issues.append(Issue(type=IssueType.SEMANTIC,
                                position=s.position,
                                message="Cannot find variable named %s" % e.what.name))
    for s in script.walk_descendants(restrict_to=SetStatement):
        if s.instance is None:
            raise Exception("We did not expected s.instance to be null for %s" % str(s.instance))
        t = compute_type(script, s.instance, issues)
        if t is None:
            raise Exception("We did not expected s.instance to be null for %s" % str(s.instance))
        if not isinstance(t, REntityRefType):
            raise Exception("We did not expected type of s.instance to be not an EntityRefType for %s" % str(t))
        if t.entity is None:
            raise Exception("We did not expected entity to be null for %s" % str(s))
        entity = t.entity
        s.feature.try_to_resolve(entity.features)
        if not s.feature.resolved():
            issues.append(Issue(type=IssueType.SEMANTIC,
                                position=s.position,
                                message="Unable to resolve feature reference in %s. Candidates: %s" % (
                                    str(s), str(entity.features))))
            return
        feature_type = compute_type(script, s.feature.referred, issues)
        value_type = compute_type(script, s.value, issues)
        if not feature_type.can_be_assigned(value_type):
            issues.append(Issue(type=IssueType.SEMANTIC,
                                position=s.position,
                                message="Cannot assign %s (type %s) to feature %s (type %s)"
                                        % (str(s.value), str(value_type), str(s.feature.referred), str(feature_type))))
    for s in script.walk_descendants(restrict_to=GetFeatureValueExpression):
        e = compute_type(script, s.instance, issues).entity
        s.feature.try_to_resolve(e.features)
