from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

if TYPE_CHECKING:
    from golem_node_api_client.models.transfer_command_body import TransferCommandBody


T = TypeVar('T', bound='TransferCommand')


@dataclass
class TransferCommand:
    """
    Attributes:
        transfer (TransferCommandBody):
    """

    transfer: 'TransferCommandBody'
    additional_properties: Dict[str, Any] = field(init=False, default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        transfer = self.transfer.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                'transfer': transfer,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from golem_node_api_client.models.transfer_command_body import TransferCommandBody

        d = src_dict.copy()
        transfer = TransferCommandBody.from_dict(d.pop('transfer'))

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
