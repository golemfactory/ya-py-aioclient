import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.activity_payment import ActivityPayment
    from ..models.agreement_payment import AgreementPayment


T = TypeVar("T", bound="Payment")


@_attrs_define
class Payment:
    """A Payment is a single transaction sent from Requestor to Provider. A single payment can be made for multiple
    Agreements and Activities. `agreementPayments` and `activityPayments` specify what is the basis for payment.

        Attributes:
            payment_id (str):
            payer_id (str):
            payee_id (str):
            payer_addr (str):
            payee_addr (str):
            payment_platform (str):
            amount (str):
            timestamp (datetime.datetime):
            agreement_payments (List['AgreementPayment']):
            activity_payments (List['ActivityPayment']):
            details (str):
    """

    payment_id: str
    payer_id: str
    payee_id: str
    payer_addr: str
    payee_addr: str
    payment_platform: str
    amount: str
    timestamp: datetime.datetime
    agreement_payments: List["AgreementPayment"]
    activity_payments: List["ActivityPayment"]
    details: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        payment_id = self.payment_id

        payer_id = self.payer_id

        payee_id = self.payee_id

        payer_addr = self.payer_addr

        payee_addr = self.payee_addr

        payment_platform = self.payment_platform

        amount = self.amount

        timestamp = self.timestamp.isoformat()

        agreement_payments = []
        for agreement_payments_item_data in self.agreement_payments:
            agreement_payments_item = agreement_payments_item_data.to_dict()
            agreement_payments.append(agreement_payments_item)

        activity_payments = []
        for activity_payments_item_data in self.activity_payments:
            activity_payments_item = activity_payments_item_data.to_dict()
            activity_payments.append(activity_payments_item)

        details = self.details

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "paymentId": payment_id,
                "payerId": payer_id,
                "payeeId": payee_id,
                "payerAddr": payer_addr,
                "payeeAddr": payee_addr,
                "paymentPlatform": payment_platform,
                "amount": amount,
                "timestamp": timestamp,
                "agreementPayments": agreement_payments,
                "activityPayments": activity_payments,
                "details": details,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.activity_payment import ActivityPayment
        from ..models.agreement_payment import AgreementPayment

        d = src_dict.copy()
        payment_id = d.pop("paymentId")

        payer_id = d.pop("payerId")

        payee_id = d.pop("payeeId")

        payer_addr = d.pop("payerAddr")

        payee_addr = d.pop("payeeAddr")

        payment_platform = d.pop("paymentPlatform")

        amount = d.pop("amount")

        timestamp = isoparse(d.pop("timestamp"))

        agreement_payments = []
        _agreement_payments = d.pop("agreementPayments")
        for agreement_payments_item_data in _agreement_payments:
            agreement_payments_item = AgreementPayment.from_dict(
                agreement_payments_item_data
            )

            agreement_payments.append(agreement_payments_item)

        activity_payments = []
        _activity_payments = d.pop("activityPayments")
        for activity_payments_item_data in _activity_payments:
            activity_payments_item = ActivityPayment.from_dict(
                activity_payments_item_data
            )

            activity_payments.append(activity_payments_item)

        details = d.pop("details")

        payment = cls(
            payment_id=payment_id,
            payer_id=payer_id,
            payee_id=payee_id,
            payer_addr=payer_addr,
            payee_addr=payee_addr,
            payment_platform=payment_platform,
            amount=amount,
            timestamp=timestamp,
            agreement_payments=agreement_payments,
            activity_payments=activity_payments,
            details=details,
        )

        payment.additional_properties = d
        return payment

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
