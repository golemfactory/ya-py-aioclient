from dataclasses import dataclass, field
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from golem_node_api_client.types import UNSET, Unset

T = TypeVar('T', bound='StartCommandBody')


@dataclass
class StartCommandBody:
    """
    Attributes:
        args (Union[Unset, List[str]]):
    """

    args: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        args: Union[Unset, List[str]] = UNSET
        if not isinstance(self.args, Unset):
            args = self.args

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if args is not UNSET:
            field_dict['args'] = args

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        args = cast(List[str], d.pop('args', UNSET))

        start_command_body = cls(
            args=args,
        )

        start_command_body.additional_properties = d
        return start_command_body

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
