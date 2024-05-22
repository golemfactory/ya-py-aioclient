from enum import Enum


class ExeScriptCommandResultResult(str, Enum):
    ERROR = 'Error'
    OK = 'Ok'

    def __str__(self) -> str:
        return str(self.value)
