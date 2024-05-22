from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Status")


@_attrs_define
class Status:
    """
    Attributes:
        node_id (str): Ethereum address (40 hexadecimal digits with "0x" prefix)
        sessions (int):
        listen_ip (Union[Unset, str]):
        public_ip (Union[Unset, str]):
    """

    node_id: str
    sessions: int
    listen_ip: Union[Unset, str] = UNSET
    public_ip: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        node_id = self.node_id

        sessions = self.sessions

        listen_ip = self.listen_ip

        public_ip = self.public_ip

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nodeId": node_id,
                "sessions": sessions,
            }
        )
        if listen_ip is not UNSET:
            field_dict["listenIp"] = listen_ip
        if public_ip is not UNSET:
            field_dict["publicIp"] = public_ip

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        node_id = d.pop("nodeId")

        sessions = d.pop("sessions")

        listen_ip = d.pop("listenIp", UNSET)

        public_ip = d.pop("publicIp", UNSET)

        status = cls(
            node_id=node_id,
            sessions=sessions,
            listen_ip=listen_ip,
            public_ip=public_ip,
        )

        status.additional_properties = d
        return status

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
