from typing import Optional, List, Union
from datetime import datetime
from typing_extensions import Literal, Final

class Network(object):
    _id: Optional[str]  # readonly: False
    ip: str  # readonly: False
    mask: Optional[str]  # readonly: False
    gateway: Optional[str]  # readonly: False

    def __init__(self,
        ip: str,
        _id: Optional[str] = None,
        mask: Optional[str] = None,
        gateway: Optional[str] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class Node(object):
    _id: str  # readonly: False
    ip: str  # readonly: False

    def __init__(self,
        _id: str,
        ip: str
    ) -> None: ...
    def to_dict(self) -> dict: ...


class ErrorMessage(object):
    message: Optional[str]  # readonly: False

    def __init__(self,
        message: Optional[str] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class Address(object):
    ip: str  # readonly: False

    def __init__(self,
        ip: str
    ) -> None: ...
    def to_dict(self) -> dict: ...


class Connection(object):
    protocol: int  # readonly: True
    local_ip: str  # readonly: True
    local_port: int  # readonly: True
    remote_ip: str  # readonly: True
    remote_port: int  # readonly: True

    def __init__(self,
        protocol: int,
        local_ip: str,
        local_port: int,
        remote_ip: str,
        remote_port: int
    ) -> None: ...
    def to_dict(self) -> dict: ...


