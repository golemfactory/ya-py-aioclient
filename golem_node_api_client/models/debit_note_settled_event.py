import datetime
from dataclasses import dataclass, field
from typing import Any, Dict, List, Type, TypeVar, Union

from dateutil.parser import isoparse

from golem_node_api_client.types import UNSET, Unset

T = TypeVar('T', bound='DebitNoteSettledEvent')


@dataclass
class DebitNoteSettledEvent:
    """
    Attributes:
        event_type (str):
        event_date (datetime.datetime):
        debit_note_id (Union[Unset, str]):
    """

    event_type: str
    event_date: datetime.datetime
    debit_note_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        event_type = self.event_type

        event_date = self.event_date.isoformat()

        debit_note_id = self.debit_note_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                'eventType': event_type,
                'eventDate': event_date,
            }
        )
        if debit_note_id is not UNSET:
            field_dict['debitNoteId'] = debit_note_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        event_type = d.pop('eventType')

        event_date = isoparse(d.pop('eventDate'))

        debit_note_id = d.pop('debitNoteId', UNSET)

        debit_note_settled_event = cls(
            event_type=event_type,
            event_date=event_date,
            debit_note_id=debit_note_id,
        )

        debit_note_settled_event.additional_properties = d
        return debit_note_settled_event

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
