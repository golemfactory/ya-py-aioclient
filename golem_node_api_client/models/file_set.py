from dataclasses import dataclass, field
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from golem_node_api_client.types import UNSET, Unset

T = TypeVar('T', bound='FileSet')


@dataclass
class FileSet:
    """
    Attributes:
        desc (Union[Unset, str]):
        includes (Union[Unset, List[str]]):
        excludes (Union[Unset, List[str]]):
    """

    desc: Union[Unset, str] = UNSET
    includes: Union[Unset, List[str]] = UNSET
    excludes: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        desc = self.desc

        includes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.includes, Unset):
            includes = self.includes

        excludes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.excludes, Unset):
            excludes = self.excludes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if desc is not UNSET:
            field_dict['desc'] = desc
        if includes is not UNSET:
            field_dict['includes'] = includes
        if excludes is not UNSET:
            field_dict['excludes'] = excludes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        desc = d.pop('desc', UNSET)

        includes = cast(List[str], d.pop('includes', UNSET))

        excludes = cast(List[str], d.pop('excludes', UNSET))

        file_set = cls(
            desc=desc,
            includes=includes,
            excludes=excludes,
        )

        file_set.additional_properties = d
        return file_set

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
