from dataclasses import dataclass, field
from typing import Any, Dict, List, Type, TypeVar, Union

from golem_node_api_client.models.rejection_reason import RejectionReason
from golem_node_api_client.types import UNSET, Unset

T = TypeVar('T', bound='Rejection')


@dataclass
class Rejection:
    """Message sent when Requestor rejects a Debit Note or Invoice.

    Attributes:
        rejection_reason (RejectionReason): Possible reasons to reject a Debit Note or Invoice.
        total_amount_accepted (str):
        message (Union[Unset, str]):
    """

    rejection_reason: RejectionReason
    total_amount_accepted: str
    message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rejection_reason = self.rejection_reason.value

        total_amount_accepted = self.total_amount_accepted

        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                'rejectionReason': rejection_reason,
                'totalAmountAccepted': total_amount_accepted,
            }
        )
        if message is not UNSET:
            field_dict['message'] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        rejection_reason = RejectionReason(d.pop('rejectionReason'))

        total_amount_accepted = d.pop('totalAmountAccepted')

        message = d.pop('message', UNSET)

        rejection = cls(
            rejection_reason=rejection_reason,
            total_amount_accepted=total_amount_accepted,
            message=message,
        )

        rejection.additional_properties = d
        return rejection

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
