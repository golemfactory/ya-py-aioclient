import datetime
from dataclasses import dataclass, field
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from dateutil.parser import isoparse

from golem_node_api_client.models.invoice_status import InvoiceStatus
from golem_node_api_client.types import UNSET, Unset

T = TypeVar('T', bound='Invoice')


@dataclass
class Invoice:
    """An Invoice is an artifact issued by the Provider to the Requestor, in the context of a specific Agreement. It
    indicates the total Amount owed by the Requestor in this Agreement. No further Debit Notes shall be issued after the
    Invoice is issued. The issue of Invoice signals the Termination of the Agreement (if it hasn't been terminated
    already). No Activity execution is allowed after the Invoice is issued.

    **NOTE:** An invoice can be issued even before any Activity is started in the context of an Agreement (eg. in one
    off, 'fire-and-forget' payment regime).

        Attributes:
            invoice_id (str):
            issuer_id (str):
            recipient_id (str):
            payee_addr (str):
            payer_addr (str):
            payment_platform (str):
            timestamp (datetime.datetime):
            agreement_id (str):
            amount (str):
            payment_due_date (datetime.datetime):
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
            activity_ids (Union[Unset, List[str]]):
    """

    invoice_id: str
    issuer_id: str
    recipient_id: str
    payee_addr: str
    payer_addr: str
    payment_platform: str
    timestamp: datetime.datetime
    agreement_id: str
    amount: str
    payment_due_date: datetime.datetime
    status: InvoiceStatus
    activity_ids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoice_id = self.invoice_id

        issuer_id = self.issuer_id

        recipient_id = self.recipient_id

        payee_addr = self.payee_addr

        payer_addr = self.payer_addr

        payment_platform = self.payment_platform

        timestamp = self.timestamp.isoformat()

        agreement_id = self.agreement_id

        amount = self.amount

        payment_due_date = self.payment_due_date.isoformat()

        status = self.status.value

        activity_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.activity_ids, Unset):
            activity_ids = self.activity_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                'invoiceId': invoice_id,
                'issuerId': issuer_id,
                'recipientId': recipient_id,
                'payeeAddr': payee_addr,
                'payerAddr': payer_addr,
                'paymentPlatform': payment_platform,
                'timestamp': timestamp,
                'agreementId': agreement_id,
                'amount': amount,
                'paymentDueDate': payment_due_date,
                'status': status,
            }
        )
        if activity_ids is not UNSET:
            field_dict['activityIds'] = activity_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        invoice_id = d.pop('invoiceId')

        issuer_id = d.pop('issuerId')

        recipient_id = d.pop('recipientId')

        payee_addr = d.pop('payeeAddr')

        payer_addr = d.pop('payerAddr')

        payment_platform = d.pop('paymentPlatform')

        timestamp = isoparse(d.pop('timestamp'))

        agreement_id = d.pop('agreementId')

        amount = d.pop('amount')

        payment_due_date = isoparse(d.pop('paymentDueDate'))

        status = InvoiceStatus(d.pop('status'))

        activity_ids = cast(List[str], d.pop('activityIds', UNSET))

        invoice = cls(
            invoice_id=invoice_id,
            issuer_id=issuer_id,
            recipient_id=recipient_id,
            payee_addr=payee_addr,
            payer_addr=payer_addr,
            payment_platform=payment_platform,
            timestamp=timestamp,
            agreement_id=agreement_id,
            amount=amount,
            payment_due_date=payment_due_date,
            status=status,
            activity_ids=activity_ids,
        )

        invoice.additional_properties = d
        return invoice

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
