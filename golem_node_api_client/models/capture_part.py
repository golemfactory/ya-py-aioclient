from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CapturePart")


@_attrs_define
class CapturePart:
    """
    Attributes:
        head (Union[Unset, float]):
        tail (Union[Unset, float]):
        head_tail (Union[Unset, float]):
    """

    head: Union[Unset, float] = UNSET
    tail: Union[Unset, float] = UNSET
    head_tail: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        head = self.head

        tail = self.tail

        head_tail = self.head_tail

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if head is not UNSET:
            field_dict["head"] = head
        if tail is not UNSET:
            field_dict["tail"] = tail
        if head_tail is not UNSET:
            field_dict["headTail"] = head_tail

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        head = d.pop("head", UNSET)

        tail = d.pop("tail", UNSET)

        head_tail = d.pop("headTail", UNSET)

        capture_part = cls(
            head=head,
            tail=tail,
            head_tail=head_tail,
        )

        capture_part.additional_properties = d
        return capture_part

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
