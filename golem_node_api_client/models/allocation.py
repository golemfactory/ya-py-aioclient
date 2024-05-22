import datetime
from dataclasses import dataclass, field
from typing import Any, Dict, List, Type, TypeVar, Union

from dateutil.parser import isoparse

from golem_node_api_client.types import UNSET, Unset

T = TypeVar('T', bound='Allocation')


@dataclass
class Allocation:
    """An Allocation is a designated sum of money reserved for the purpose of making some particular payments. Allocations
    are currently purely virtual objects. They exist only in Requestor's database. An Allocation is connected to a
    payment account (wallet) specified by `address` and `paymentPlatform` field. If these fields are not present the
    default payment platform is used and the address is assumed to be identical to the Requestor's Node ID.

    **NOTE:** `timeout` and `makeDeposit` field are currently ignored.

        Attributes:
            allocation_id (str):
            total_amount (str):
            spent_amount (str):
            remaining_amount (str):
            timestamp (datetime.datetime):
            make_deposit (bool):
            address (Union[Unset, str]):
            payment_platform (Union[Unset, str]):
            timeout (Union[Unset, datetime.datetime]):
    """

    allocation_id: str
    total_amount: str
    spent_amount: str
    remaining_amount: str
    timestamp: datetime.datetime
    make_deposit: bool
    address: Union[Unset, str] = UNSET
    payment_platform: Union[Unset, str] = UNSET
    timeout: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        allocation_id = self.allocation_id

        total_amount = self.total_amount

        spent_amount = self.spent_amount

        remaining_amount = self.remaining_amount

        timestamp = self.timestamp.isoformat()

        make_deposit = self.make_deposit

        address = self.address

        payment_platform = self.payment_platform

        timeout: Union[Unset, str] = UNSET
        if not isinstance(self.timeout, Unset):
            timeout = self.timeout.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                'allocationId': allocation_id,
                'totalAmount': total_amount,
                'spentAmount': spent_amount,
                'remainingAmount': remaining_amount,
                'timestamp': timestamp,
                'makeDeposit': make_deposit,
            }
        )
        if address is not UNSET:
            field_dict['address'] = address
        if payment_platform is not UNSET:
            field_dict['paymentPlatform'] = payment_platform
        if timeout is not UNSET:
            field_dict['timeout'] = timeout

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        allocation_id = d.pop('allocationId')

        total_amount = d.pop('totalAmount')

        spent_amount = d.pop('spentAmount')

        remaining_amount = d.pop('remainingAmount')

        timestamp = isoparse(d.pop('timestamp'))

        make_deposit = d.pop('makeDeposit')

        address = d.pop('address', UNSET)

        payment_platform = d.pop('paymentPlatform', UNSET)

        _timeout = d.pop('timeout', UNSET)
        timeout: Union[Unset, datetime.datetime]
        if isinstance(_timeout, Unset):
            timeout = UNSET
        else:
            timeout = isoparse(_timeout)

        allocation = cls(
            allocation_id=allocation_id,
            total_amount=total_amount,
            spent_amount=spent_amount,
            remaining_amount=remaining_amount,
            timestamp=timestamp,
            make_deposit=make_deposit,
            address=address,
            payment_platform=payment_platform,
            timeout=timeout,
        )

        allocation.additional_properties = d
        return allocation

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
