from enum import Enum


class ActivityStateStateItem(str, Enum):
    DEPLOYED = 'Deployed'
    INITIALIZED = 'Initialized'
    NEW = 'New'
    READY = 'Ready'
    TERMINATED = 'Terminated'
    UNRESPONSIVE = 'Unresponsive'

    def __str__(self) -> str:
        return str(self.value)
