from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

if TYPE_CHECKING:
    from golem_node_api_client.models.runtime_event_kind_finished_body import (
        RuntimeEventKindFinishedBody,
    )


T = TypeVar('T', bound='RuntimeEventKindFinished')


@dataclass
class RuntimeEventKindFinished:
    """
    Attributes:
        finished (RuntimeEventKindFinishedBody):
    """

    finished: 'RuntimeEventKindFinishedBody'
    additional_properties: Dict[str, Any] = field(init=False, default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        finished = self.finished.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                'finished': finished,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from golem_node_api_client.models.runtime_event_kind_finished_body import (
            RuntimeEventKindFinishedBody,
        )

        d = src_dict.copy()
        finished = RuntimeEventKindFinishedBody.from_dict(d.pop('finished'))

        runtime_event_kind_finished = cls(
            finished=finished,
        )

        runtime_event_kind_finished.additional_properties = d
        return runtime_event_kind_finished

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
