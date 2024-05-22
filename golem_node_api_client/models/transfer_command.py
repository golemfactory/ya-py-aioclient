from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.transfer_command_body import TransferCommandBody


T = TypeVar("T", bound="TransferCommand")


@_attrs_define
class TransferCommand:
    """
    Attributes:
        transfer (TransferCommandBody):
    """

    transfer: "TransferCommandBody"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        transfer = self.transfer.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "transfer": transfer,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.transfer_command_body import TransferCommandBody

        d = src_dict.copy()
        transfer = TransferCommandBody.from_dict(d.pop("transfer"))

        transfer_command = cls(
            transfer=transfer,
        )

        transfer_command.additional_properties = d
        return transfer_command

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
