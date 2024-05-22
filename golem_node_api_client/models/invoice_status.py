from enum import Enum


class InvoiceStatus(str, Enum):
    ACCEPTED = "ACCEPTED"
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"
    ISSUED = "ISSUED"
    RECEIVED = "RECEIVED"
    REJECTED = "REJECTED"
    SETTLED = "SETTLED"

    def __str__(self) -> str:
        return str(self.value)
