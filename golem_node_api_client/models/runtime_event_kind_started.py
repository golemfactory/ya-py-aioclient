from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.exe_script_command import ExeScriptCommand


T = TypeVar("T", bound="RuntimeEventKindStarted")


@_attrs_define
class RuntimeEventKindStarted:
    """
    Attributes:
        started (ExeScriptCommand):  The specification of ExeScript commands format as per Activity API specification.
            Including TRANSFER command syntax extension described in [this
            specification](https://github.com/golemfactory/golem-architecture/blob/master/GIPS/GIP-PR0001-multifile-
            transfer.md).
            ## Implementation Notes
            The schemas have been defined to accept a following format of JSON command collections:
            ``` [ { "deploy": { "net": [{ "id": "id", "ip": "10.0.0.2", "mask": "255.255.0.0" }], "hosts": {"master":
            "10.0.0.1"}, "nodes": {"10.0.0.1": "0xdeadbeef"} } }, { "start": { "args": [] } }, { "transfer": { "from":
            "http://34.244.4.185:8000/LICENSE", "to": "container:/input/file_in", "format": "zip", "depth": 2, "fileset":
            [{"desc":"all images", "includes": ["*.jpg"], "excludes": ["db*.*"] }] } }, { "run": { "entry_point": "rust-
            wasi-tutorial", "args": ["/input/file_in", "/output/file_cp"], "capture": { "stdout": {"stream": {}}, "stderr":
            {"stream": {}} } } }, { "sign": {} }, { "terminate": {} }, ... ] ```
            ### Rust
            For Rust - this format is a default representation of Rust enum types, as serialized by `serde` library.
            Therefore it is recommended to use this yaml specification to manually specify Rust enum types rather than
            depend on automatically-generated code.
    """

    started: "ExeScriptCommand"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        started = self.started.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "started": started,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.exe_script_command import ExeScriptCommand

        d = src_dict.copy()
        started = ExeScriptCommand.from_dict(d.pop("started"))

        runtime_event_kind_started = cls(
            started=started,
        )

        runtime_event_kind_started.additional_properties = d
        return runtime_event_kind_started

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
