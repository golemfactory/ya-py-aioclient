from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Connection")


@_attrs_define
class Connection:
    """
    Attributes:
        protocol (int):
        local_ip (str):
        local_port (int):
        remote_ip (str):
        remote_port (int):
    """

    protocol: int
    local_ip: str
    local_port: int
    remote_ip: str
    remote_port: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        protocol = self.protocol

        local_ip = self.local_ip

        local_port = self.local_port

        remote_ip = self.remote_ip

        remote_port = self.remote_port

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "protocol": protocol,
                "localIp": local_ip,
                "localPort": local_port,
                "remoteIp": remote_ip,
                "remotePort": remote_port,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        protocol = d.pop("protocol")

        local_ip = d.pop("localIp")

        local_port = d.pop("localPort")

        remote_ip = d.pop("remoteIp")

        remote_port = d.pop("remotePort")

        connection = cls(
            protocol=protocol,
            local_ip=local_ip,
            local_port=local_port,
            remote_ip=remote_ip,
            remote_port=remote_port,
        )

        connection.additional_properties = d
        return connection

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
