from dataclasses import dataclass, field
from typing import Any, Dict, List, Type, TypeVar

T = TypeVar('T', bound='DeployNetwork')


@dataclass
class DeployNetwork:
    """
    Attributes:
        id (str):
        ip (str):
        mask (str):
    """

    id: str
    ip: str
    mask: str
    additional_properties: Dict[str, Any] = field(init=False, default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        ip = self.ip

        mask = self.mask

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                'id': id,
                'ip': ip,
                'mask': mask,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop('id')

        ip = d.pop('ip')

        mask = d.pop('mask')

        deploy_network = cls(
            id=id,
            ip=ip,
            mask=mask,
        )

        deploy_network.additional_properties = d
        return deploy_network

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
