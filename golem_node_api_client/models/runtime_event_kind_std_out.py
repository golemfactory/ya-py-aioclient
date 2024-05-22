from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.command_output import CommandOutput


T = TypeVar("T", bound="RuntimeEventKindStdOut")


@_attrs_define
class RuntimeEventKindStdOut:
    """
    Attributes:
        stdout (CommandOutput):
    """

    stdout: "CommandOutput"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        stdout = self.stdout.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stdout": stdout,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.command_output import CommandOutput

        d = src_dict.copy()
        stdout = CommandOutput.from_dict(d.pop("stdout"))

        runtime_event_kind_std_out = cls(
            stdout=stdout,
        )

        runtime_event_kind_std_out.additional_properties = d
        return runtime_event_kind_std_out

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
