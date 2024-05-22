from dataclasses import dataclass, field
from typing import Any, Dict, List, Type, TypeVar, Union

from golem_node_api_client.types import UNSET, Unset

T = TypeVar('T', bound='ActivityPayment')


@dataclass
class ActivityPayment:
    """Share of a Payment assigned to a particular Activity.

    Attributes:
        activity_id (str):
        amount (str):
        allocation_id (Union[Unset, str]):
    """

    activity_id: str
    amount: str
    allocation_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        activity_id = self.activity_id

        amount = self.amount

        allocation_id = self.allocation_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                'activityId': activity_id,
                'amount': amount,
            }
        )
        if allocation_id is not UNSET:
            field_dict['allocationId'] = allocation_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        activity_id = d.pop('activityId')

        amount = d.pop('amount')

        allocation_id = d.pop('allocationId', UNSET)

        activity_payment = cls(
            activity_id=activity_id,
            amount=amount,
            allocation_id=allocation_id,
        )

        activity_payment.additional_properties = d
        return activity_payment

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
