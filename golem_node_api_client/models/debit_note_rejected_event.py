import datetime
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from dateutil.parser import isoparse

from golem_node_api_client.types import UNSET, Unset

if TYPE_CHECKING:
    from golem_node_api_client.models.rejection import Rejection


T = TypeVar('T', bound='DebitNoteRejectedEvent')


@dataclass
class DebitNoteRejectedEvent:
    """
    Attributes:
        event_type (str):
        event_date (datetime.datetime):
        debit_note_id (Union[Unset, str]):
        rejection (Union[Unset, Rejection]): Message sent when Requestor rejects a Debit Note or Invoice.
    """

    event_type: str
    event_date: datetime.datetime
    debit_note_id: Union[Unset, str] = UNSET
    rejection: Union[Unset, 'Rejection'] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        event_type = self.event_type

        event_date = self.event_date.isoformat()

        debit_note_id = self.debit_note_id

        rejection: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rejection, Unset):
            rejection = self.rejection.to_dict()

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
        if rejection is not UNSET:
            field_dict['rejection'] = rejection

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from golem_node_api_client.models.rejection import Rejection

        d = src_dict.copy()
        event_type = d.pop('eventType')

        event_date = isoparse(d.pop('eventDate'))

        debit_note_id = d.pop('debitNoteId', UNSET)

        _rejection = d.pop('rejection', UNSET)
        rejection: Union[Unset, Rejection]
        if isinstance(_rejection, Unset):
            rejection = UNSET
        else:
            rejection = Rejection.from_dict(_rejection)

        debit_note_rejected_event = cls(
            event_type=event_type,
            event_date=event_date,
            debit_note_id=debit_note_id,
            rejection=rejection,
        )

        debit_note_rejected_event.additional_properties = d
        return debit_note_rejected_event

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
