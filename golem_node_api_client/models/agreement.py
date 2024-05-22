import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.agreement_state import AgreementState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.demand import Demand
    from ..models.offer import Offer


T = TypeVar("T", bound="Agreement")


@_attrs_define
class Agreement:
    """
    Attributes:
        agreement_id (str):
        demand (Demand):
        offer (Offer):
        valid_to (datetime.datetime): End of validity period.

            Agreement needs to be approved, rejected or cancelled before this date; otherwise will expire.
        state (AgreementState): * `Proposal` - newly created by a Requestor (draft based on Proposal)
            * `Pending` - confirmed by a Requestor and send to Provider for approval
            * `Cancelled` by a Requestor
            * `Rejected` by a Provider
            * `Approved` by both sides
            * `Expired` - not approved, rejected nor cancelled within validity period
            * `Terminated` - finished after approval.
        timestamp (datetime.datetime):
        approved_date (Union[Unset, datetime.datetime]): Agreement approval timestamp
        app_session_id (Union[Unset, str]): A correlation/session identifier used for querying events related to an
            action where this appSessionId has been specified.
        proposed_signature (Union[Unset, str]):
        approved_signature (Union[Unset, str]):
        committed_signature (Union[Unset, str]):
    """

    agreement_id: str
    demand: "Demand"
    offer: "Offer"
    valid_to: datetime.datetime
    state: AgreementState
    timestamp: datetime.datetime
    approved_date: Union[Unset, datetime.datetime] = UNSET
    app_session_id: Union[Unset, str] = UNSET
    proposed_signature: Union[Unset, str] = UNSET
    approved_signature: Union[Unset, str] = UNSET
    committed_signature: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        agreement_id = self.agreement_id

        demand = self.demand.to_dict()

        offer = self.offer.to_dict()

        valid_to = self.valid_to.isoformat()

        state = self.state.value

        timestamp = self.timestamp.isoformat()

        approved_date: Union[Unset, str] = UNSET
        if not isinstance(self.approved_date, Unset):
            approved_date = self.approved_date.isoformat()

        app_session_id = self.app_session_id

        proposed_signature = self.proposed_signature

        approved_signature = self.approved_signature

        committed_signature = self.committed_signature

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agreementId": agreement_id,
                "demand": demand,
                "offer": offer,
                "validTo": valid_to,
                "state": state,
                "timestamp": timestamp,
            }
        )
        if approved_date is not UNSET:
            field_dict["approvedDate"] = approved_date
        if app_session_id is not UNSET:
            field_dict["appSessionId"] = app_session_id
        if proposed_signature is not UNSET:
            field_dict["proposedSignature"] = proposed_signature
        if approved_signature is not UNSET:
            field_dict["approvedSignature"] = approved_signature
        if committed_signature is not UNSET:
            field_dict["committedSignature"] = committed_signature

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.demand import Demand
        from ..models.offer import Offer

        d = src_dict.copy()
        agreement_id = d.pop("agreementId")

        demand = Demand.from_dict(d.pop("demand"))

        offer = Offer.from_dict(d.pop("offer"))

        valid_to = isoparse(d.pop("validTo"))

        state = AgreementState(d.pop("state"))

        timestamp = isoparse(d.pop("timestamp"))

        _approved_date = d.pop("approvedDate", UNSET)
        approved_date: Union[Unset, datetime.datetime]
        if isinstance(_approved_date, Unset):
            approved_date = UNSET
        else:
            approved_date = isoparse(_approved_date)

        app_session_id = d.pop("appSessionId", UNSET)

        proposed_signature = d.pop("proposedSignature", UNSET)

        approved_signature = d.pop("approvedSignature", UNSET)

        committed_signature = d.pop("committedSignature", UNSET)

        agreement = cls(
            agreement_id=agreement_id,
            demand=demand,
            offer=offer,
            valid_to=valid_to,
            state=state,
            timestamp=timestamp,
            approved_date=approved_date,
            app_session_id=app_session_id,
            proposed_signature=proposed_signature,
            approved_signature=approved_signature,
            committed_signature=committed_signature,
        )

        agreement.additional_properties = d
        return agreement

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
