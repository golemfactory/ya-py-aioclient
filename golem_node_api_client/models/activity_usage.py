from dataclasses import dataclass, field
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from golem_node_api_client.types import UNSET, Unset

T = TypeVar('T', bound='ActivityUsage')


@dataclass
class ActivityUsage:
    """
    Attributes:
        timestamp (int): Usage update timestamp (UTC)
        current_usage (Union[Unset, List[float]]): Current vector of usage counters consumed by the Activity. The
            sequence of values corresponds to Usage Vector property (golem.usage.vector) as indicated in the Agreement
            (Offer part). Example: [123.5, 34000].
    """

    timestamp: int
    current_usage: Union[Unset, List[float]] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        timestamp = self.timestamp

        current_usage: Union[Unset, List[float]] = UNSET
        if not isinstance(self.current_usage, Unset):
            current_usage = self.current_usage

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                'timestamp': timestamp,
            }
        )
        if current_usage is not UNSET:
            field_dict['currentUsage'] = current_usage

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        timestamp = d.pop('timestamp')

        current_usage = cast(List[float], d.pop('currentUsage', UNSET))

        activity_usage = cls(
            timestamp=timestamp,
            current_usage=current_usage,
        )

        activity_usage.additional_properties = d
        return activity_usage

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
