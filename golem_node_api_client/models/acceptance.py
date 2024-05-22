from dataclasses import dataclass, field
from typing import Any, Dict, List, Type, TypeVar

T = TypeVar('T', bound='Acceptance')


@dataclass
class Acceptance:
    """Message sent when Requestor accepts a Debit Note or Invoice.

    Attributes:
        total_amount_accepted (str):
        allocation_id (str):
    """

    total_amount_accepted: str
    allocation_id: str
    additional_properties: Dict[str, Any] = field(init=False, default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_amount_accepted = self.total_amount_accepted

        allocation_id = self.allocation_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                'totalAmountAccepted': total_amount_accepted,
                'allocationId': allocation_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total_amount_accepted = d.pop('totalAmountAccepted')

        allocation_id = d.pop('allocationId')

        acceptance = cls(
            total_amount_accepted=total_amount_accepted,
            allocation_id=allocation_id,
        )

        acceptance.additional_properties = d
        return acceptance

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
