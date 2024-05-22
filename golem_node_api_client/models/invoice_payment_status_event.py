import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.driver_status_property import DriverStatusProperty


T = TypeVar("T", bound="InvoicePaymentStatusEvent")


@_attrs_define
class InvoicePaymentStatusEvent:
    """
    Attributes:
        event_type (str):
        event_date (datetime.datetime):
        invoice_id (Union[Unset, str]):
        property_ (Union[Unset, DriverStatusProperty]): Individual actionable property of the payment driver status
    """

    event_type: str
    event_date: datetime.datetime
    invoice_id: Union[Unset, str] = UNSET
    property_: Union[Unset, "DriverStatusProperty"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        event_type = self.event_type

        event_date = self.event_date.isoformat()

        invoice_id = self.invoice_id

        property_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.property_, Unset):
            property_ = self.property_.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "eventType": event_type,
                "eventDate": event_date,
            }
        )
        if invoice_id is not UNSET:
            field_dict["invoiceId"] = invoice_id
        if property_ is not UNSET:
            field_dict["property"] = property_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.driver_status_property import DriverStatusProperty

        d = src_dict.copy()
        event_type = d.pop("eventType")

        event_date = isoparse(d.pop("eventDate"))

        invoice_id = d.pop("invoiceId", UNSET)

        _property_ = d.pop("property", UNSET)
        property_: Union[Unset, DriverStatusProperty]
        if isinstance(_property_, Unset):
            property_ = UNSET
        else:
            property_ = DriverStatusProperty.from_dict(_property_)

        invoice_payment_status_event = cls(
            event_type=event_type,
            event_date=event_date,
            invoice_id=invoice_id,
            property_=property_,
        )

        invoice_payment_status_event.additional_properties = d
        return invoice_payment_status_event

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
