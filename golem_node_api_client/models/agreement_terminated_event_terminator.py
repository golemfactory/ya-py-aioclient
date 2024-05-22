from enum import Enum


class AgreementTerminatedEventTerminator(str, Enum):
    PROVIDER = "Provider"
    REQUESTOR = "Requestor"

    def __str__(self) -> str:
        return str(self.value)
