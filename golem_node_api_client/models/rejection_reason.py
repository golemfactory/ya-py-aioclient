from enum import Enum


class RejectionReason(str, Enum):
    BAD_SERVICE = "BAD_SERVICE"
    INCORRECT_AMOUNT = "INCORRECT_AMOUNT"
    UNSOLICITED_SERVICE = "UNSOLICITED_SERVICE"

    def __str__(self) -> str:
        return str(self.value)
