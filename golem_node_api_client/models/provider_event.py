import datetime
from dataclasses import dataclass, field
from typing import Any, Dict, List, Type, TypeVar

from dateutil.parser import isoparse

T = TypeVar('T', bound='ProviderEvent')


@dataclass
class ProviderEvent:
    """
    Attributes:
        event_type (str):
        event_date (datetime.datetime):
        activity_id (str):
        agreement_id (str):
    """

    event_type: str
    event_date: datetime.datetime
    activity_id: str
    agreement_id: str
    additional_properties: Dict[str, Any] = field(init=False, default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        event_type = self.event_type

        event_date = self.event_date.isoformat()

        activity_id = self.activity_id

        agreement_id = self.agreement_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                'eventType': event_type,
                'eventDate': event_date,
                'activityId': activity_id,
                'agreementId': agreement_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        event_type = d.pop('eventType')

        event_date = isoparse(d.pop('eventDate'))

        activity_id = d.pop('activityId')

        agreement_id = d.pop('agreementId')

        provider_event = cls(
            event_type=event_type,
            event_date=event_date,
            activity_id=activity_id,
            agreement_id=agreement_id,
        )

        provider_event.additional_properties = d
        return provider_event

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
