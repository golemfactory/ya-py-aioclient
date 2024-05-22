from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.runtime_event_kind import RuntimeEventKind


T = TypeVar("T", bound="RuntimeEvent")


@_attrs_define
class RuntimeEvent:
    """Structure returned as data element of event stream.

    Attributes:
        batch_id (str):
        index (int):
        timestamp (str):
        kind (RuntimeEventKind):
    """

    batch_id: str
    index: int
    timestamp: str
    kind: "RuntimeEventKind"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        batch_id = self.batch_id

        index = self.index

        timestamp = self.timestamp

        kind = self.kind.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "batchId": batch_id,
                "index": index,
                "timestamp": timestamp,
                "kind": kind,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.runtime_event_kind import RuntimeEventKind

        d = src_dict.copy()
        batch_id = d.pop("batchId")

        index = d.pop("index")

        timestamp = d.pop("timestamp")

        kind = RuntimeEventKind.from_dict(d.pop("kind"))

        runtime_event = cls(
            batch_id=batch_id,
            index=index,
            timestamp=timestamp,
            kind=kind,
        )

        runtime_event.additional_properties = d
        return runtime_event

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
