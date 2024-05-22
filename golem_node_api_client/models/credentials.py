from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

if TYPE_CHECKING:
    from golem_node_api_client.models.sgx_credentials import SgxCredentials


T = TypeVar('T', bound='Credentials')


@dataclass
class Credentials:
    """
    Attributes:
        sgx (SgxCredentials):
    """

    sgx: 'SgxCredentials'
    additional_properties: Dict[str, Any] = field(init=False, default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sgx = self.sgx.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                'sgx': sgx,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from golem_node_api_client.models.sgx_credentials import SgxCredentials

        d = src_dict.copy()
        sgx = SgxCredentials.from_dict(d.pop('sgx'))

        credentials = cls(
            sgx=sgx,
        )

        credentials.additional_properties = d
        return credentials

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
