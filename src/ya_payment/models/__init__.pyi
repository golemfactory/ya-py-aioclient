from typing import Optional, List
from datetime import datetime
from typing_extensions import Literal, Final

class DebitNoteEvent(object):
    debit_note_id: str  # readonly: False
    timestamp: datetime  # readonly: False
    details: dict  # readonly: False
    event_type: EventType  # readonly: False

    def __init__(self,
        debit_note_id: str,
        timestamp: datetime,
        event_type: EventType,
        details: dict = None
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


class Invoice(object):
    invoice_id: str  # readonly: True
    issuer_id: str  # readonly: True
    recipient_id: str  # readonly: True
    payee_addr: Optional[str]  # readonly: True
    payer_addr: Optional[str]  # readonly: True
    payment_platform: Optional[str]  # readonly: True
    last_debit_note_id: Optional[str]  # readonly: True
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
        timestamp: datetime,
        agreement_id: str,
        amount: str,
        payment_due_date: datetime,
        status: InvoiceStatus,
        payee_addr: Optional[str] = None,
        payer_addr: Optional[str] = None,
        payment_platform: Optional[str] = None,
        last_debit_note_id: Optional[str] = None,
        activity_ids: Optional[list] = None
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


class Acceptance(object):
    total_amount_accepted: str  # readonly: False
    allocation_id: str  # readonly: False

    def __init__(self,
        total_amount_accepted: str,
        allocation_id: str
    ) -> None: ...
    def to_dict(self) -> dict: ...


class ErrorMessage(object):
    message: Optional[str]  # readonly: False

    def __init__(self,
        message: Optional[str] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class InvoiceEvent(object):
    invoice_id: str  # readonly: False
    timestamp: datetime  # readonly: False
    details: dict  # readonly: False
    event_type: EventType  # readonly: False

    def __init__(self,
        invoice_id: str,
        timestamp: datetime,
        event_type: EventType,
        details: dict = None
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


class DebitNote(object):
    debit_note_id: str  # readonly: True
    issuer_id: str  # readonly: True
    recipient_id: str  # readonly: True
    payee_addr: Optional[str]  # readonly: True
    payer_addr: Optional[str]  # readonly: True
    payment_platform: Optional[str]  # readonly: True
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
        timestamp: datetime,
        agreement_id: str,
        activity_id: str,
        total_amount_due: str,
        status: InvoiceStatus,
        payee_addr: Optional[str] = None,
        payer_addr: Optional[str] = None,
        payment_platform: Optional[str] = None,
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
    timeout: Optional[datetime]  # readonly: False
    make_deposit: bool  # readonly: False

    def __init__(self,
        allocation_id: str,
        total_amount: str,
        spent_amount: str,
        remaining_amount: str,
        make_deposit: bool,
        address: Optional[str] = None,
        payment_platform: Optional[str] = None,
        timeout: Optional[datetime] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class RejectionReason:
    UNSOLICITED_SERVICE: Final = 'UNSOLICITED_SERVICE'
    BAD_SERVICE: Final = 'BAD_SERVICE'
    INCORRECT_AMOUNT: Final = 'INCORRECT_AMOUNT'


class EventType:
    RECEIVED: Final = 'RECEIVED'
    ACCEPTED: Final = 'ACCEPTED'
    REJECTED: Final = 'REJECTED'
    CANCELLED: Final = 'CANCELLED'


