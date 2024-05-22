from dataclasses import dataclass, field
from typing import Any, Dict, List, Type, TypeVar

T = TypeVar('T', bound='Account')


@dataclass
class Account:
    """Payment account (wallet)

    Attributes:
        platform (str):
        address (str):
        driver (str):
        network (str):
        token (str):
        send (bool):
        receive (bool):
    """

    platform: str
    address: str
    driver: str
    network: str
    token: str
    send: bool
    receive: bool
    additional_properties: Dict[str, Any] = field(init=False, default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        platform = self.platform

        address = self.address

        driver = self.driver

        network = self.network

        token = self.token

        send = self.send

        receive = self.receive

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                'platform': platform,
                'address': address,
                'driver': driver,
                'network': network,
                'token': token,
                'send': send,
                'receive': receive,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        platform = d.pop('platform')

        address = d.pop('address')

        driver = d.pop('driver')

        network = d.pop('network')

        token = d.pop('token')

        send = d.pop('send')

        receive = d.pop('receive')

        account = cls(
            platform=platform,
            address=address,
            driver=driver,
            network=network,
            token=token,
            send=send,
            receive=receive,
        )

        account.additional_properties = d
        return account

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
