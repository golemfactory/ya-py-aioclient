from typing import Optional, List, Union
from datetime import datetime
from typing_extensions import Literal, Final

class Acceptance(object):
    total_amount_accepted: str  # readonly: False
    allocation_id: str  # readonly: False

    def __init__(self,
        total_amount_accepted: str,
        allocation_id: str
    ) -> None: ...
    def to_dict(self) -> dict: ...


class InvoiceEvent(object):
    event_type: str  # readonly: False
    event_date: datetime  # readonly: False

    def __init__(self,
        event_type: str,
        event_date: datetime
    ) -> None: ...
    def to_dict(self) -> dict: ...


class MarketProperty(object):
    key: str  # readonly: False
    value: str  # readonly: False

    def __init__(self,
        key: str,
        value: str
    ) -> None: ...
    def to_dict(self) -> dict: ...


class ErrorMessage(object):
    message: Optional[str]  # readonly: False

    def __init__(self,
        message: Optional[str] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class MarketDecoration(object):
    properties: list  # readonly: False
    constraints: list  # readonly: False

    def __init__(self,
        properties: list,
        constraints: list
    ) -> None: ...
    def to_dict(self) -> dict: ...


class Account(object):
    platform: str  # readonly: False
    address: str  # readonly: False
    driver: str  # readonly: False
    network: str  # readonly: False
    token: str  # readonly: False
    send: bool  # readonly: False
    receive: bool  # readonly: False

    def __init__(self,
        platform: str,
        address: str,
        driver: str,
        network: str,
        token: str,
        send: bool,
        receive: bool
    ) -> None: ...
    def to_dict(self) -> dict: ...


class Rejection(object):
    rejection_reason: RejectionReason  # readonly: False
    total_amount_accepted: str  # readonly: False
    message: Optional[str]  # readonly: False

    def __init__(self,
        rejection_reason: RejectionReason,
        total_amount_accepted: str,
        message: Optional[str] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class Payment(object):
    payment_id: str  # readonly: False
    payer_id: str  # readonly: False
    payee_id: str  # readonly: False
    payer_addr: str  # readonly: False
    payee_addr: str  # readonly: False
    payment_platform: str  # readonly: False
    amount: str  # readonly: False
    timestamp: datetime  # readonly: False
    agreement_payments: list  # readonly: False
    activity_payments: list  # readonly: False
    details: str  # readonly: False

    def __init__(self,
        payment_id: str,
        payer_id: str,
        payee_id: str,
        payer_addr: str,
        payee_addr: str,
        payment_platform: str,
        amount: str,
        timestamp: datetime,
        agreement_payments: list,
        activity_payments: list,
        details: str
    ) -> None: ...
    def to_dict(self) -> dict: ...


class DebitNoteEvent(object):
    event_type: str  # readonly: False
    event_date: datetime  # readonly: False

    def __init__(self,
        event_type: str,
        event_date: datetime
    ) -> None: ...
    def to_dict(self) -> dict: ...


class DebitNote(object):
    debit_note_id: str  # readonly: True
    issuer_id: str  # readonly: True
    recipient_id: str  # readonly: True
    payee_addr: str  # readonly: True
    payer_addr: str  # readonly: True
    payment_platform: str  # readonly: True
    previous_debit_note_id: Optional[str]  # readonly: True
    timestamp: datetime  # readonly: True
    agreement_id: str  # readonly: True
    activity_id: str  # readonly: False
    total_amount_due: str  # readonly: False
    usage_counter_vector: dict  # readonly: False
    payment_due_date: Optional[datetime]  # readonly: False
    status: InvoiceStatus  # readonly: False

    def __init__(self,
        debit_note_id: str,
        issuer_id: str,
        recipient_id: str,
        payee_addr: str,
        payer_addr: str,
        payment_platform: str,
        timestamp: datetime,
        agreement_id: str,
        activity_id: str,
        total_amount_due: str,
        status: InvoiceStatus,
        previous_debit_note_id: Optional[str] = None,
        usage_counter_vector: dict = None,
        payment_due_date: Optional[datetime] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class Allocation(object):
    allocation_id: str  # readonly: True
    address: Optional[str]  # readonly: False
    payment_platform: Optional[str]  # readonly: False
    total_amount: str  # readonly: False
    spent_amount: str  # readonly: True
    remaining_amount: str  # readonly: True
    timestamp: datetime  # readonly: True
    timeout: Optional[datetime]  # readonly: False
    make_deposit: bool  # readonly: False

    def __init__(self,
        allocation_id: str,
        total_amount: str,
        spent_amount: str,
        remaining_amount: str,
        timestamp: datetime,
        make_deposit: bool,
        address: Optional[str] = None,
        payment_platform: Optional[str] = None,
        timeout: Optional[datetime] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class AgreementPayment(object):
    agreement_id: str  # readonly: False
    amount: str  # readonly: False
    allocation_id: Optional[str]  # readonly: False

    def __init__(self,
        agreement_id: str,
        amount: str,
        allocation_id: Optional[str] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class Invoice(object):
    invoice_id: str  # readonly: True
    issuer_id: str  # readonly: True
    recipient_id: str  # readonly: True
    payee_addr: str  # readonly: True
    payer_addr: str  # readonly: True
    payment_platform: str  # readonly: True
    timestamp: datetime  # readonly: True
    agreement_id: str  # readonly: False
    activity_ids: Optional[list]  # readonly: False
    amount: str  # readonly: False
    payment_due_date: datetime  # readonly: False
    status: InvoiceStatus  # readonly: False

    def __init__(self,
        invoice_id: str,
        issuer_id: str,
        recipient_id: str,
        payee_addr: str,
        payer_addr: str,
        payment_platform: str,
        timestamp: datetime,
        agreement_id: str,
        amount: str,
        payment_due_date: datetime,
        status: InvoiceStatus,
        activity_ids: Optional[list] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class InvoiceStatus:
    ISSUED: Final = 'ISSUED'
    RECEIVED: Final = 'RECEIVED'
    ACCEPTED: Final = 'ACCEPTED'
    REJECTED: Final = 'REJECTED'
    FAILED: Final = 'FAILED'
    SETTLED: Final = 'SETTLED'
    CANCELLED: Final = 'CANCELLED'


class ActivityPayment(object):
    activity_id: str  # readonly: False
    amount: str  # readonly: False
    allocation_id: Optional[str]  # readonly: False

    def __init__(self,
        activity_id: str,
        amount: str,
        allocation_id: Optional[str] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class RejectionReason:
    UNSOLICITED_SERVICE: Final = 'UNSOLICITED_SERVICE'
    BAD_SERVICE: Final = 'BAD_SERVICE'
    INCORRECT_AMOUNT: Final = 'INCORRECT_AMOUNT'


class InvoiceRejectedEventAllOf(InvoiceEvent):
    invoice_id: Optional[str]  # readonly: False
    rejection: Rejection  # readonly: False

    def __init__(self,
        event_type: str,
        event_date: datetime,
        invoice_id: Optional[str] = None,
        rejection: Rejection = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class InvoiceReceivedEvent(InvoiceEvent):
    invoice_id: Optional[str]  # readonly: False

    def __init__(self,
        event_type: str,
        event_date: datetime,
        invoice_id: Optional[str] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class DebitNoteRejectedEvent(DebitNoteEvent):
    debit_note_id: Optional[str]  # readonly: False
    rejection: Rejection  # readonly: False

    def __init__(self,
        event_type: str,
        event_date: datetime,
        debit_note_id: Optional[str] = None,
        rejection: Rejection = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class DebitNoteCancelledEvent(DebitNoteEvent):
    debit_note_id: Optional[str]  # readonly: False

    def __init__(self,
        event_type: str,
        event_date: datetime,
        debit_note_id: Optional[str] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class InvoiceCancelledEvent(InvoiceEvent):
    invoice_id: Optional[str]  # readonly: False

    def __init__(self,
        event_type: str,
        event_date: datetime,
        invoice_id: Optional[str] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class PaymentReceivedEvent(InvoiceEvent):
    payment_id: Optional[str]  # readonly: False

    def __init__(self,
        event_type: str,
        event_date: datetime,
        payment_id: Optional[str] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class InvoiceSettledEvent(InvoiceEvent):
    invoice_id: Optional[str]  # readonly: False

    def __init__(self,
        event_type: str,
        event_date: datetime,
        invoice_id: Optional[str] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class PaymentReceivedEventAllOf(InvoiceEvent):
    payment_id: Optional[str]  # readonly: False

    def __init__(self,
        event_type: str,
        event_date: datetime,
        payment_id: Optional[str] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class DebitNoteReceivedEvent(DebitNoteEvent):
    debit_note_id: Optional[str]  # readonly: False

    def __init__(self,
        event_type: str,
        event_date: datetime,
        debit_note_id: Optional[str] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class DebitNoteReceivedEventAllOf(DebitNoteEvent):
    debit_note_id: Optional[str]  # readonly: False

    def __init__(self,
        event_type: str,
        event_date: datetime,
        debit_note_id: Optional[str] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class DebitNoteSettledEvent(DebitNoteEvent):
    debit_note_id: Optional[str]  # readonly: False

    def __init__(self,
        event_type: str,
        event_date: datetime,
        debit_note_id: Optional[str] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class DebitNoteFailedEvent(DebitNoteEvent):
    debit_note_id: Optional[str]  # readonly: False

    def __init__(self,
        event_type: str,
        event_date: datetime,
        debit_note_id: Optional[str] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class DebitNoteRejectedEventAllOf(DebitNoteEvent):
    debit_note_id: Optional[str]  # readonly: False
    rejection: Rejection  # readonly: False

    def __init__(self,
        event_type: str,
        event_date: datetime,
        debit_note_id: Optional[str] = None,
        rejection: Rejection = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class InvoiceRejectedEvent(InvoiceEvent):
    invoice_id: Optional[str]  # readonly: False
    rejection: Rejection  # readonly: False

    def __init__(self,
        event_type: str,
        event_date: datetime,
        invoice_id: Optional[str] = None,
        rejection: Rejection = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class InvoiceReceivedEventAllOf(InvoiceEvent):
    invoice_id: Optional[str]  # readonly: False

    def __init__(self,
        event_type: str,
        event_date: datetime,
        invoice_id: Optional[str] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class DebitNoteAcceptedEvent(DebitNoteEvent):
    debit_note_id: Optional[str]  # readonly: False

    def __init__(self,
        event_type: str,
        event_date: datetime,
        debit_note_id: Optional[str] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class InvoiceAcceptedEvent(InvoiceEvent):
    invoice_id: Optional[str]  # readonly: False

    def __init__(self,
        event_type: str,
        event_date: datetime,
        invoice_id: Optional[str] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class InvoiceFailedEvent(InvoiceEvent):
    invoice_id: Optional[str]  # readonly: False

    def __init__(self,
        event_type: str,
        event_date: datetime,
        invoice_id: Optional[str] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


