from enum import Enum


class CaptureFormat(str, Enum):
    BINARY = "binary"
    STRING = "string"

    def __str__(self) -> str:
        return str(self.value)
