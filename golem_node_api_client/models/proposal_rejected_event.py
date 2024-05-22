import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reason import Reason


T = TypeVar("T", bound="ProposalRejectedEvent")


@_attrs_define
class ProposalRejectedEvent:
    """
    Attributes:
        event_type (str):
        event_date (datetime.datetime):
        proposal_id (str):
        reason (Union[Unset, Reason]): Generic Event reason information structure.
    """

    event_type: str
    event_date: datetime.datetime
    proposal_id: str
    reason: Union[Unset, "Reason"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        event_type = self.event_type

        event_date = self.event_date.isoformat()

        proposal_id = self.proposal_id

        reason: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "eventType": event_type,
                "eventDate": event_date,
                "proposalId": proposal_id,
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

        proposal_id = d.pop("proposalId")

        _reason = d.pop("reason", UNSET)
        reason: Union[Unset, Reason]
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = Reason.from_dict(_reason)

        proposal_rejected_event = cls(
            event_type=event_type,
            event_date=event_date,
            proposal_id=proposal_id,
            reason=reason,
        )

        proposal_rejected_event.additional_properties = d
        return proposal_rejected_event

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
