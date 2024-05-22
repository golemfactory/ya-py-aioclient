from dataclasses import dataclass, field
from typing import Any, Dict, List, Type, TypeVar, Union

from golem_node_api_client.types import UNSET, Unset

T = TypeVar('T', bound='Network')


@dataclass
class Network:
    """
    Attributes:
        ip (str):
        id (Union[Unset, str]):
        mask (Union[Unset, str]):
        gateway (Union[Unset, str]):
    """

    ip: str
    id: Union[Unset, str] = UNSET
    mask: Union[Unset, str] = UNSET
    gateway: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ip = self.ip

        id = self.id

        mask = self.mask

        gateway = self.gateway

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                'ip': ip,
            }
        )
        if id is not UNSET:
            field_dict['id'] = id
        if mask is not UNSET:
            field_dict['mask'] = mask
        if gateway is not UNSET:
            field_dict['gateway'] = gateway

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ip = d.pop('ip')

        id = d.pop('id', UNSET)

        mask = d.pop('mask', UNSET)

        gateway = d.pop('gateway', UNSET)

        network = cls(
            ip=ip,
            id=id,
            mask=mask,
            gateway=gateway,
        )

        network.additional_properties = d
        return network

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
