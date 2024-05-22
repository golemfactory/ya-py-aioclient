from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AgreementPayment")


@_attrs_define
class AgreementPayment:
    """Share of a Payment assigned to an Agreement, but not to any particular Activity within that Agreement.

    Attributes:
        agreement_id (str):
        amount (str):
        allocation_id (Union[Unset, str]):
    """

    agreement_id: str
    amount: str
    allocation_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        agreement_id = self.agreement_id

        amount = self.amount

        allocation_id = self.allocation_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agreementId": agreement_id,
                "amount": amount,
            }
        )
        if allocation_id is not UNSET:
            field_dict["allocationId"] = allocation_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        agreement_id = d.pop("agreementId")

        amount = d.pop("amount")

        allocation_id = d.pop("allocationId", UNSET)

        agreement_payment = cls(
            agreement_id=agreement_id,
            amount=amount,
            allocation_id=allocation_id,
        )

        agreement_payment.additional_properties = d
        return agreement_payment

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
