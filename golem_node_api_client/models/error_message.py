from dataclasses import dataclass, field
from typing import Any, Dict, List, Type, TypeVar, Union

from golem_node_api_client.types import UNSET, Unset

T = TypeVar('T', bound='ErrorMessage')


@dataclass
class ErrorMessage:
    """Generic Error Message structure.

    Attributes:
        message (Union[Unset, str]):
    """

    message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict['message'] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        message = d.pop('message', UNSET)

        error_message = cls(
            message=message,
        )

        error_message.additional_properties = d
        return error_message

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
