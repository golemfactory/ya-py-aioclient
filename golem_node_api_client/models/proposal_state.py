from enum import Enum


class ProposalState(str, Enum):
    ACCEPTED = "Accepted"
    DRAFT = "Draft"
    EXPIRED = "Expired"
    INITIAL = "Initial"
    REJECTED = "Rejected"

    def __str__(self) -> str:
        return str(self.value)
