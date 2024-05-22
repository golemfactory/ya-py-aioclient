from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ExeScriptCommand")


@_attrs_define
class ExeScriptCommand:
    """The specification of ExeScript commands format as per Activity API specification. Including TRANSFER command syntax
    extension described in [this specification](https://github.com/golemfactory/golem-architecture/blob/master/GIPS/GIP-
    PR0001-multifile-transfer.md).
    ## Implementation Notes
    The schemas have been defined to accept a following format of JSON command collections:
    ``` [ { "deploy": { "net": [{ "id": "id", "ip": "10.0.0.2", "mask": "255.255.0.0" }], "hosts": {"master":
    "10.0.0.1"}, "nodes": {"10.0.0.1": "0xdeadbeef"} } }, { "start": { "args": [] } }, { "transfer": { "from":
    "http://34.244.4.185:8000/LICENSE", "to": "container:/input/file_in", "format": "zip", "depth": 2, "fileset":
    [{"desc":"all images", "includes": ["*.jpg"], "excludes": ["db*.*"] }] } }, { "run": { "entry_point": "rust-wasi-
    tutorial", "args": ["/input/file_in", "/output/file_cp"], "capture": { "stdout": {"stream": {}}, "stderr":
    {"stream": {}} } } }, { "sign": {} }, { "terminate": {} }, ... ] ```
    ### Rust
    For Rust - this format is a default representation of Rust enum types, as serialized by `serde` library. Therefore
    it is recommended to use this yaml specification to manually specify Rust enum types rather than depend on
    automatically-generated code.

    """

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        exe_script_command = cls()

        exe_script_command.additional_properties = d
        return exe_script_command

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
