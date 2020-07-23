from pathlib import Path
from typing import Any, List, Optional, Dict, Iterator, Union, TypeVar, Type
from typing_extensions import Final
from collections import OrderedDict
from dataclasses import dataclass, field
from any_case import to_snake_case  # type: ignore
import yaml

REF_PREFIX = "#/components/schemas/"
GENERATED_INDENT: Final = " " * 4


class JsonObject(Dict[str, Union[str, float, int, bool, "JsonObject"]]):
    pass


T = TypeVar("T")


def check_type(_type: Type[T], value: Any) -> Optional[T]:
    return value if isinstance(value, _type) else None


def force_type(_type: Type[T], value: Any, *err_info) -> T:
    if not isinstance(value, _type):
        raise RuntimeError(*err_info)
    return value


@dataclass
class PropertyInfo:
    type: str
    format: Optional[str]
    description: Optional[str]
    required: bool
    read_only: bool

    @staticmethod
    def from_dict(
        data: JsonObject, ref_type: Optional["ModelInfo"] = None, required: bool = False
    ) -> "PropertyInfo":
        if ref_type:
            _type = ref_type.name
        else:
            _type = force_type(str, data.get("type"), "fail to decode type info", data)

        read_only = force_type(
            bool, data.get("readOnly", False), "readOnly should be bool", data
        )
        format = check_type(str, data.get("format"))
        description = check_type(str, data.get("description"))

        _enum = data.get("enum")
        if _enum:
            assert isinstance(_enum, list)
            return EnumPropertyInfo(
                type=_type,
                format=format,
                description=description,
                read_only=read_only,
                values=_enum,
                required=required,
            )
        else:
            return PropertyInfo(
                type=_type,
                format=format,
                description=description,
                read_only=read_only,
                required=required,
            )

    def option(self, value: str) -> str:
        return value if self.required else f"Optional[{value}]"

    def union(self, *values: str) -> str:
        if self.required:
            return f'Union[{",".join("None", *values)}]'
        else:
            return f'Union[{",".join(values)}]'

    def base_name(self) -> str:
        if self.type == "string" and self.format == "date-time":
            return self.option(f"datetime")
        if self.type == "boolean":
            return self.option('bool')
        if self.type == "string":
            return self.option("str")
        if self.type == "array":
            return self.option("list")
        if self.type == "integer":
            return self.option("int")
        if self.type == "number":
            if self.format == "int64" or self.format == "int64":
                return self.option("int")
            if self.format == "float" or self.format == "double":
                return self.option("float")
            return "Union[float, int]"
        if self.type == "object":
            return "dict"
        # print('type=', self)
        return self.type


@dataclass
class EnumPropertyInfo(PropertyInfo):
    values: List[str]

    def base_name(self) -> str:
        values = ",".join(f'"{value}"' for value in self.values)
        return f"Literal[{values}]"


@dataclass
class ModelInfo:
    name: str
    base: List["ModelInfo"] = field(default_factory=list)
    props: Dict[str, PropertyInfo] = field(default_factory=OrderedDict)
    resolved: bool = False
    enum: Optional[List[Any]] = None

    def init_args(self) -> Iterator[str]:
        props: Dict[str, PropertyInfo] = {}
        for base in self.base:
            props.update(**base.props)
        props.update(**self.props)

        required = [k for (k, p) in props.items() if p.required]
        optional = [k for (k, p) in props.items() if not p.required]
        for name in required + optional:
            prop = props[name]
            _type = prop.base_name()
            if prop.required:
                yield f"{GENERATED_INDENT}{GENERATED_INDENT}{to_snake_case(name)}: {_type}"
            else:
                yield f"{GENERATED_INDENT}{GENERATED_INDENT}{to_snake_case(name)}: {_type} = None"

    def gen_enum(self) -> Iterator[str]:
        assert self.enum is not None

        yield f'class {self.name}:'
        for item in self.enum:
            yield f'{GENERATED_INDENT}{to_snake_case(item).upper()}: Final = {repr(item)}'
        yield ''
        yield ''

    def gen_code(self) -> Iterator[str]:
        if self.enum:
            yield from self.gen_enum()
        else:
            yield from self.gen_object()

    def gen_object(self) -> Iterator[str]:
        bases = ",".join(base.name for base in self.base) if self.base else "object"
        yield f"class {self.name}({bases}):"
        for name in self.props:
            prop = self.props[name]
            yield f"{GENERATED_INDENT}{to_snake_case(name)}: {prop.base_name()}  # readonly: {prop.read_only}"
        yield ""
        init_args = ",\n".join(self.init_args())
        if init_args:
            yield f"{GENERATED_INDENT}def __init__(self,"
            yield f"{init_args}"
            yield f"{GENERATED_INDENT}) -> None: ..."
        else:
            yield f"{GENERATED_INDENT}def __init__(self) -> None: ..."
        yield f"{GENERATED_INDENT}def to_dict(self) -> dict: ..."
        yield ""
        yield ""


def resolve_type(
    ctx: Dict[str, ModelInfo], name: str, *specs: Dict[str, Any]
) -> Optional[ModelInfo]:
    def find_spec(_name: str) -> Optional[Dict[str, Any]]:
        for spec in specs:
            _s = spec.get("schemas")
            if not _s:
                _s = spec["components"]["schemas"]
            item_spec = _s.get(_name)
            if item_spec:
                return item_spec
        return None

    type_info = find_spec(name)
    if not type_info and name.endswith("AllOf"):
        type_info = find_spec(name[:-5])

    info = ctx.get(name) or ModelInfo(name)
    if name not in ctx:
        ctx[name] = info

    if info.resolved:
        return info

    _enum = type_info.get('enum')
    if _enum:
        info.enum = _enum
        info.resolved = True
        return info

    def resolve_ref(_r: str) -> ModelInfo:
        if not _r.startswith(REF_PREFIX):
            idx = _r.find(REF_PREFIX)
            if not idx or idx < 0:
                raise RuntimeError("invalid type reference", _r)
            _r = _r[idx:]
        base_type_name = _r[len(REF_PREFIX) :]
        base_type = ctx.get(base_type_name) or ModelInfo(base_type_name)
        if base_type_name not in ctx:
            ctx[base_type_name] = base_type
        return base_type

    if not type_info:
        return None
    if "allOf" in type_info:
        for definition in type_info["allOf"]:
            _ref = definition.get("$ref")
            _type = definition.get("type", None)
            if _ref:
                assert isinstance(_ref, str)
                assert _ref.startswith(REF_PREFIX)
                info.base.append(resolve_ref(_ref))
            elif _type == "object":
                _properties = definition.get("properties", dict())
                for prop_name in _properties:
                    prop_def = _properties[prop_name]
                    _prop_ref = prop_def.get("$ref")
                    _ref_type = resolve_ref(_prop_ref) if _prop_ref else None

                    info.props[prop_name] = PropertyInfo.from_dict(
                        prop_def, ref_type=_ref_type
                    )
    else:
        _type = type_info.get("type")
        if _type == "object":
            required = set(type_info.get("required") or list())
            _properties = type_info.get("properties", dict())
            for prop_name in _properties:
                prop_def = _properties[prop_name]
                _prop_ref = prop_def.get("$ref")
                _ref_type = resolve_ref(_prop_ref) if _prop_ref else None
                info.props[prop_name] = PropertyInfo.from_dict(
                    _properties[prop_name],
                    ref_type=_ref_type,
                    required=(prop_name in required),
                )

    info.resolved = True
    return info


def gen_model(module: Any, *specs: Dict[str, Any]) -> Iterator[str]:
    ctx: Dict[str, ModelInfo] = OrderedDict()

    for item_name in dir(module):
        it = getattr(module, item_name)
        types = getattr(it, "openapi_types", None)
        if not types:
            continue
        info = resolve_type(ctx, item_name, *specs)
        if not info:
            raise RuntimeError("unable to resolve", item_name)

    unresolved: List[str] = list(
        name for (name, model) in ctx.items() if not model.resolved
    )
    while unresolved:
        for name in unresolved:
            resolve_type(ctx, name, *specs)
        unresolved = list(name for (name, model) in ctx.items() if not model.resolved)

    unordered_names = set(ctx.keys())
    ordered_names = list()

    def is_free(name: str) -> bool:
        model = ctx[name]
        for base in model.base:
            if base.name not in ordered_names:
                return False
        return True

    while unordered_names:
        free_names = [name for name in unordered_names if is_free(name)]
        if not free_names:
            free_names = [next(iter(unordered_names))]
        for name in free_names:
            ordered_names.append(name)
            unordered_names.remove(name)

    yield """from typing import Optional, List
from datetime import datetime
from typing_extensions import Literal, Final
"""
    for name in ordered_names:
        info = ctx[name]
        yield from info.gen_code()


def load_spec(file_name: Union[str, Path]) -> JsonObject:
    with open(file_name) as f:
        return yaml.load(f, Loader=yaml.FullLoader)


def main(*modules: str):
    import importlib
    build_dir = Path("ya-client/specs")
    common_spec = load_spec(build_dir / "common.yaml")

    for module_name in modules:
        print(f'loading spec for: {module_name}')
        spec = load_spec(build_dir / f"{module_name}-api.yaml")
        print(f"loading module for {module_name}")
        module = importlib.import_module(f"ya_{module_name}")
        module_models = getattr(module, 'models')
        with open(f"src/ya_{module_name}/models/__init__.pyi", "w") as out_f:
            for line in gen_model(module_models, spec, common_spec):
                out_f.write(f"{line}\n")
                print(line)


if __name__ == "__main__":
    import sys
    main(*sys.argv[1:])
