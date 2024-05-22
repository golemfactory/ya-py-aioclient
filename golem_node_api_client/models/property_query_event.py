import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.property_query import PropertyQuery


T = TypeVar("T", bound="PropertyQueryEvent")


@_attrs_define
class PropertyQueryEvent:
    """
    Attributes:
        event_type (str):
        event_date (datetime.datetime):
        property_query (PropertyQuery):
    """

    event_type: str
    event_date: datetime.datetime
    property_query: "PropertyQuery"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        event_type = self.event_type

        event_date = self.event_date.isoformat()

        property_query = self.property_query.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "eventType": event_type,
                "eventDate": event_date,
                "propertyQuery": property_query,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.property_query import PropertyQuery

        d = src_dict.copy()
        event_type = d.pop("eventType")

        event_date = isoparse(d.pop("eventDate"))

        property_query = PropertyQuery.from_dict(d.pop("propertyQuery"))

        property_query_event = cls(
            event_type=event_type,
            event_date=event_date,
            property_query=property_query,
        )

        property_query_event.additional_properties = d
        return property_query_event

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
