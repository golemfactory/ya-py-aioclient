from dataclasses import dataclass, field
from typing import Any, Dict, List, Type, TypeVar, Union

from golem_node_api_client.types import UNSET, Unset

T = TypeVar('T', bound='CreateActivityRequest')


@dataclass
class CreateActivityRequest:
    """
    Attributes:
        agreement_id (str):
        requestor_pub_key (Union[Unset, str]):
    """

    agreement_id: str
    requestor_pub_key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        agreement_id = self.agreement_id

        requestor_pub_key = self.requestor_pub_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                'agreementId': agreement_id,
            }
        )
        if requestor_pub_key is not UNSET:
            field_dict['requestorPubKey'] = requestor_pub_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        agreement_id = d.pop('agreementId')

        requestor_pub_key = d.pop('requestorPubKey', UNSET)

        create_activity_request = cls(
            agreement_id=agreement_id,
            requestor_pub_key=requestor_pub_key,
        )

        create_activity_request.additional_properties = d
        return create_activity_request

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
