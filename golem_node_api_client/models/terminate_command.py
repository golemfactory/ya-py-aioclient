from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.terminate_command_body import TerminateCommandBody


T = TypeVar("T", bound="TerminateCommand")


@_attrs_define
class TerminateCommand:
    """
    Attributes:
        terminate (TerminateCommandBody):
    """

    terminate: "TerminateCommandBody"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        terminate = self.terminate.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "terminate": terminate,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.terminate_command_body import TerminateCommandBody

        d = src_dict.copy()
        terminate = TerminateCommandBody.from_dict(d.pop("terminate"))

        terminate_command = cls(
            terminate=terminate,
        )

        terminate_command.additional_properties = d
        return terminate_command

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
