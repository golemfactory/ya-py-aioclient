from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.capture_format import CaptureFormat
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.capture_part import CapturePart


T = TypeVar("T", bound="CaptureAtEndBody")


@_attrs_define
class CaptureAtEndBody:
    """
    Attributes:
        part (Union[Unset, CapturePart]):
        format_ (Union[Unset, CaptureFormat]):
    """

    part: Union[Unset, "CapturePart"] = UNSET
    format_: Union[Unset, CaptureFormat] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        part: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.part, Unset):
            part = self.part.to_dict()

        format_: Union[Unset, str] = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if part is not UNSET:
            field_dict["part"] = part
        if format_ is not UNSET:
            field_dict["format"] = format_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.capture_part import CapturePart

        d = src_dict.copy()
        _part = d.pop("part", UNSET)
        part: Union[Unset, CapturePart]
        if isinstance(_part, Unset):
            part = UNSET
        else:
            part = CapturePart.from_dict(_part)

        _format_ = d.pop("format", UNSET)
        format_: Union[Unset, CaptureFormat]
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = CaptureFormat(_format_)

        capture_at_end_body = cls(
            part=part,
            format_=format_,
        )

        capture_at_end_body.additional_properties = d
        return capture_at_end_body

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
