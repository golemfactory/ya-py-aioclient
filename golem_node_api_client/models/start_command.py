from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.start_command_body import StartCommandBody


T = TypeVar("T", bound="StartCommand")


@_attrs_define
class StartCommand:
    """
    Attributes:
        start (Union[Unset, StartCommandBody]):
    """

    start: Union[Unset, "StartCommandBody"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        start: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start is not UNSET:
            field_dict["start"] = start

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.start_command_body import StartCommandBody

        d = src_dict.copy()
        _start = d.pop("start", UNSET)
        start: Union[Unset, StartCommandBody]
        if isinstance(_start, Unset):
            start = UNSET
        else:
            start = StartCommandBody.from_dict(_start)

        start_command = cls(
            start=start,
        )

        start_command.additional_properties = d
        return start_command

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
