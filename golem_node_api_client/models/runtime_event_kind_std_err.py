from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.command_output import CommandOutput


T = TypeVar("T", bound="RuntimeEventKindStdErr")


@_attrs_define
class RuntimeEventKindStdErr:
    """
    Attributes:
        stderr (CommandOutput):
    """

    stderr: "CommandOutput"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        stderr = self.stderr.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stderr": stderr,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.command_output import CommandOutput

        d = src_dict.copy()
        stderr = CommandOutput.from_dict(d.pop("stderr"))

        runtime_event_kind_std_err = cls(
            stderr=stderr,
        )

        runtime_event_kind_std_err.additional_properties = d
        return runtime_event_kind_std_err

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
