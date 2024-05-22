import datetime
from dataclasses import dataclass, field
from typing import Any, Dict, List, Type, TypeVar, Union

from dateutil.parser import isoparse

from golem_node_api_client.types import UNSET, Unset

T = TypeVar('T', bound='AllocationUpdate')


@dataclass
class AllocationUpdate:
    """AllocationUpdate represents the changes that can be made to an existing allocation.

    Attributes:
        total_amount (Union[Unset, str]):
        timeout (Union[Unset, datetime.datetime]):
    """

    total_amount: Union[Unset, str] = UNSET
    timeout: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_amount = self.total_amount

        timeout: Union[Unset, str] = UNSET
        if not isinstance(self.timeout, Unset):
            timeout = self.timeout.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_amount is not UNSET:
            field_dict['totalAmount'] = total_amount
        if timeout is not UNSET:
            field_dict['timeout'] = timeout

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total_amount = d.pop('totalAmount', UNSET)

        _timeout = d.pop('timeout', UNSET)
        timeout: Union[Unset, datetime.datetime]
        if isinstance(_timeout, Unset):
            timeout = UNSET
        else:
            timeout = isoparse(_timeout)

        allocation_update = cls(
            total_amount=total_amount,
            timeout=timeout,
        )

        allocation_update.additional_properties = d
        return allocation_update

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
