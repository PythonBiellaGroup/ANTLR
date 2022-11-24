from jinja2 import Environment, PackageLoader, select_autoescape

from pylasu.model import Node
from pylasu.support import extension_method

from parsers.entities_parser import StringType, IntegerType, EntityRefType

env = Environment(
    loader=PackageLoader("code_generators"),
    autoescape=select_autoescape())


@extension_method(Node)
def to_python(self: Node) -> str:
    template = env.get_template(f"{self.node_type.__name__.lower()}.txt")
    return template.render(node=self)


@extension_method(EntityRefType)
def to_python(self: EntityRefType) -> str:
    return f'"{self.entity.name}"'


@extension_method(IntegerType)
def to_python(self: IntegerType) -> str:
    return "int"


@extension_method(StringType)
def to_python(self: StringType) -> str:
    return "str"
