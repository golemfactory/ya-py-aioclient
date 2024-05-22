import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.agreement_terminated_event_terminator import (
    AgreementTerminatedEventTerminator,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reason import Reason


T = TypeVar("T", bound="AgreementTerminatedEvent")


@_attrs_define
class AgreementTerminatedEvent:
    """
    Attributes:
        event_type (str):
        event_date (datetime.datetime):
        agreement_id (str):
        terminator (AgreementTerminatedEventTerminator):
        signature (str):
        reason (Union[Unset, Reason]): Generic Event reason information structure.
    """

    event_type: str
    event_date: datetime.datetime
    agreement_id: str
    terminator: AgreementTerminatedEventTerminator
    signature: str
    reason: Union[Unset, "Reason"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        event_type = self.event_type

        event_date = self.event_date.isoformat()

        agreement_id = self.agreement_id

        terminator = self.terminator.value

        signature = self.signature

        reason: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "eventType": event_type,
                "eventDate": event_date,
                "agreementId": agreement_id,
                "terminator": terminator,
                "signature": signature,
            }
        )
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.reason import Reason

        d = src_dict.copy()
        event_type = d.pop("eventType")

        event_date = isoparse(d.pop("eventDate"))

        agreement_id = d.pop("agreementId")

        terminator = AgreementTerminatedEventTerminator(d.pop("terminator"))

        signature = d.pop("signature")

        _reason = d.pop("reason", UNSET)
        reason: Union[Unset, Reason]
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = Reason.from_dict(_reason)

        agreement_terminated_event = cls(
            event_type=event_type,
            event_date=event_date,
            agreement_id=agreement_id,
            terminator=terminator,
            signature=signature,
            reason=reason,
        )

        agreement_terminated_event.additional_properties = d
        return agreement_terminated_event

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
