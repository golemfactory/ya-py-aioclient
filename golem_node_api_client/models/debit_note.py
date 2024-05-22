import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.invoice_status import InvoiceStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.debit_note_usage_counter_vector import DebitNoteUsageCounterVector


T = TypeVar("T", bound="DebitNote")


@_attrs_define
class DebitNote:
    """A Debit Note is an artifact issued by the Provider to the Requestor, in the context of a specific Activity. It is a
    notification of Total Amount Due incurred by the Activity until the moment the Debit Note is issued. This is
    expected to be used as trigger for payment in upfront-payment or pay-as-you-go scenarios.

    **NOTE:** Only Debit Notes with non-null paymentDueDate are expected to trigger payments.

    **NOTE:** Debit Notes flag the current Total Amount Due, which is accumulated from the start of Activity. Debit
    Notes are expected to trigger payments, therefore payment amount for the newly received Debit Note is expected to be
    determined by difference of Total Payments for the Agreement vs Total Amount Due.

        Attributes:
            debit_note_id (str):
            issuer_id (str):
            recipient_id (str):
            payee_addr (str):
            payer_addr (str):
            payment_platform (str):
            timestamp (datetime.datetime):
            agreement_id (str):
            activity_id (str):
            total_amount_due (str):
            status (InvoiceStatus): Accepted status indicates that the Requestor confirms the Amount/Total Amount Due on the
                Invoice/Debit Note, respectively. The Payment API Implementation is expected to proceed with the orchestration
                of the payment. Internals of the payment processing (e.g. payment processing internal states) are specific to
                the selected Payment Platform, and must be indicated as an attribute of the Accepted status. However, as they
                are specific - they shall not be standardized by the Payment API.

                A Rejected Invoice/Debit Note can subsequently be Accepted.

                An Accepted Invoice/Debit Note cannot be subsequently Rejected.

                There is a difference between Paid and Settled - depending on a Payment Platform. Paid indicates that the
                Requestor has ordered Payments of Total Amount Due as indicated by received/accepted Debit Notes/Invoice.
                Settled indicates that the Provider has reliably received the Payments.

                **WARNING:** 'Paid' status currently not implemented.
            previous_debit_note_id (Union[Unset, str]):
            usage_counter_vector (Union[Unset, DebitNoteUsageCounterVector]):
            payment_due_date (Union[Unset, datetime.datetime]):
    """

    debit_note_id: str
    issuer_id: str
    recipient_id: str
    payee_addr: str
    payer_addr: str
    payment_platform: str
    timestamp: datetime.datetime
    agreement_id: str
    activity_id: str
    total_amount_due: str
    status: InvoiceStatus
    previous_debit_note_id: Union[Unset, str] = UNSET
    usage_counter_vector: Union[Unset, "DebitNoteUsageCounterVector"] = UNSET
    payment_due_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        debit_note_id = self.debit_note_id

        issuer_id = self.issuer_id

        recipient_id = self.recipient_id

        payee_addr = self.payee_addr

        payer_addr = self.payer_addr

        payment_platform = self.payment_platform

        timestamp = self.timestamp.isoformat()

        agreement_id = self.agreement_id

        activity_id = self.activity_id

        total_amount_due = self.total_amount_due

        status = self.status.value

        previous_debit_note_id = self.previous_debit_note_id

        usage_counter_vector: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.usage_counter_vector, Unset):
            usage_counter_vector = self.usage_counter_vector.to_dict()

        payment_due_date: Union[Unset, str] = UNSET
        if not isinstance(self.payment_due_date, Unset):
            payment_due_date = self.payment_due_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "debitNoteId": debit_note_id,
                "issuerId": issuer_id,
                "recipientId": recipient_id,
                "payeeAddr": payee_addr,
                "payerAddr": payer_addr,
                "paymentPlatform": payment_platform,
                "timestamp": timestamp,
                "agreementId": agreement_id,
                "activityId": activity_id,
                "totalAmountDue": total_amount_due,
                "status": status,
            }
        )
        if previous_debit_note_id is not UNSET:
            field_dict["previousDebitNoteId"] = previous_debit_note_id
        if usage_counter_vector is not UNSET:
            field_dict["usageCounterVector"] = usage_counter_vector
        if payment_due_date is not UNSET:
            field_dict["paymentDueDate"] = payment_due_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.debit_note_usage_counter_vector import DebitNoteUsageCounterVector

        d = src_dict.copy()
        debit_note_id = d.pop("debitNoteId")

        issuer_id = d.pop("issuerId")

        recipient_id = d.pop("recipientId")

        payee_addr = d.pop("payeeAddr")

        payer_addr = d.pop("payerAddr")

        payment_platform = d.pop("paymentPlatform")

        timestamp = isoparse(d.pop("timestamp"))

        agreement_id = d.pop("agreementId")

        activity_id = d.pop("activityId")

        total_amount_due = d.pop("totalAmountDue")

        status = InvoiceStatus(d.pop("status"))

        previous_debit_note_id = d.pop("previousDebitNoteId", UNSET)

        _usage_counter_vector = d.pop("usageCounterVector", UNSET)
        usage_counter_vector: Union[Unset, DebitNoteUsageCounterVector]
        if isinstance(_usage_counter_vector, Unset):
            usage_counter_vector = UNSET
        else:
            usage_counter_vector = DebitNoteUsageCounterVector.from_dict(
                _usage_counter_vector
            )

        _payment_due_date = d.pop("paymentDueDate", UNSET)
        payment_due_date: Union[Unset, datetime.datetime]
        if isinstance(_payment_due_date, Unset):
            payment_due_date = UNSET
        else:
            payment_due_date = isoparse(_payment_due_date)

        debit_note = cls(
            debit_note_id=debit_note_id,
            issuer_id=issuer_id,
            recipient_id=recipient_id,
            payee_addr=payee_addr,
            payer_addr=payer_addr,
            payment_platform=payment_platform,
            timestamp=timestamp,
            agreement_id=agreement_id,
            activity_id=activity_id,
            total_amount_due=total_amount_due,
            status=status,
            previous_debit_note_id=previous_debit_note_id,
            usage_counter_vector=usage_counter_vector,
            payment_due_date=payment_due_date,
        )

        debit_note.additional_properties = d
        return debit_note

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
