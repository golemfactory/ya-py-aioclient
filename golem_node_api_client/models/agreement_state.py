from enum import Enum


class AgreementState(str, Enum):
    APPROVED = "Approved"
    CANCELLED = "Cancelled"
    EXPIRED = "Expired"
    PENDING = "Pending"
    PROPOSAL = "Proposal"
    REJECTED = "Rejected"
    TERMINATED = "Terminated"

    def __str__(self) -> str:
        return str(self.value)
