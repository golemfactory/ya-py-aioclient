from dataclasses import dataclass, field
from typing import Any, Dict, List, Type, TypeVar

T = TypeVar('T', bound='Address')


@dataclass
class Address:
    """
    Attributes:
        ip (str):
    """

    ip: str
    additional_properties: Dict[str, Any] = field(init=False, default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ip = self.ip

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                'ip': ip,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ip = d.pop('ip')

        address = cls(
            ip=ip,
        )

        address.additional_properties = d
        return address

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
