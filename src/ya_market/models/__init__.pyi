from typing import Optional, List, Union
from datetime import datetime
from typing_extensions import Literal, Final

class Agreement(object):
    agreement_id: str  # readonly: False
    demand: Demand  # readonly: False
    offer: Offer  # readonly: False
    valid_to: AgreementValidTo  # readonly: False
    approved_date: Optional[datetime]  # readonly: False
    state: Literal["Proposal","Pending","Cancelled","Rejected","Approved","Expired","Terminated"]  # readonly: False
    timestamp: Timestamp  # readonly: False
    app_session_id: AppSessionId  # readonly: False
    proposed_signature: Optional[str]  # readonly: False
    approved_signature: Optional[str]  # readonly: False
    committed_signature: Optional[str]  # readonly: False

    def __init__(self,
        agreement_id: str,
        demand: Demand,
        offer: Offer,
        valid_to: AgreementValidTo,
        state: Literal["Proposal","Pending","Cancelled","Rejected","Approved","Expired","Terminated"],
        timestamp: Timestamp,
        approved_date: Optional[datetime] = None,
        app_session_id: AppSessionId = None,
        proposed_signature: Optional[str] = None,
        approved_signature: Optional[str] = None,
        committed_signature: Optional[str] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class AgreementOperationEvent(object):
    event_type: str  # readonly: False
    event_date: Timestamp  # readonly: False
    agreement_id: str  # readonly: False

    def __init__(self,
        event_type: str,
        event_date: Timestamp,
        agreement_id: str
    ) -> None: ...
    def to_dict(self) -> dict: ...


class PropertyQuery(object):
    issuer_properties: dict  # readonly: False
    query_id: Optional[str]  # readonly: False
    queried_properties: list  # readonly: False

    def __init__(self,
        queried_properties: list,
        issuer_properties: dict = None,
        query_id: Optional[str] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class Timestamp(object):

    def __init__(self) -> None: ...
    def to_dict(self) -> dict: ...


class Event(object):
    event_type: str  # readonly: False
    event_date: Timestamp  # readonly: False

    def __init__(self,
        event_type: str,
        event_date: Timestamp
    ) -> None: ...
    def to_dict(self) -> dict: ...


class AgreementValidTo(object):

    def __init__(self) -> None: ...
    def to_dict(self) -> dict: ...


class ErrorMessage(object):
    message: Optional[str]  # readonly: False

    def __init__(self,
        message: Optional[str] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class AppSessionId(object):

    def __init__(self) -> None: ...
    def to_dict(self) -> dict: ...


class AgreementProposal(object):
    proposal_id: str  # readonly: False
    valid_to: AgreementValidTo  # readonly: False

    def __init__(self,
        proposal_id: str,
        valid_to: AgreementValidTo
    ) -> None: ...
    def to_dict(self) -> dict: ...


class Reason(object):
    message: str  # readonly: False

    def __init__(self,
        message: str
    ) -> None: ...
    def to_dict(self) -> dict: ...


class DemandOfferBase(object):
    properties: dict  # readonly: False
    constraints: str  # readonly: False

    def __init__(self,
        properties: dict,
        constraints: str
    ) -> None: ...
    def to_dict(self) -> dict: ...


class ProposalRejectedEventAllOf(Event):
    proposal_id: Optional[str]  # readonly: True
    reason: Reason  # readonly: False

    def __init__(self,
        event_type: str,
        event_date: Timestamp,
        proposal_id: Optional[str] = None,
        reason: Reason = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class AgreementEventAllOf(Event):
    agreement: Agreement  # readonly: False

    def __init__(self,
        event_type: str,
        event_date: Timestamp,
        agreement: Agreement = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class AgreementCancelledEvent(AgreementOperationEvent):
    reason: Reason  # readonly: False

    def __init__(self,
        event_type: str,
        event_date: Timestamp,
        agreement_id: str,
        reason: Reason = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class PropertyQueryEvent(Event):
    property_query: PropertyQuery  # readonly: False

    def __init__(self,
        event_type: str,
        event_date: Timestamp,
        property_query: PropertyQuery = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class Offer(DemandOfferBase):
    offer_id: Optional[str]  # readonly: True
    provider_id: Optional[str]  # readonly: True
    timestamp: Timestamp  # readonly: False

    def __init__(self,
        properties: dict,
        constraints: str,
        offer_id: Optional[str] = None,
        provider_id: Optional[str] = None,
        timestamp: Timestamp = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class ProposalEvent(Event):
    proposal: Proposal  # readonly: False

    def __init__(self,
        event_type: str,
        event_date: Timestamp,
        proposal: Proposal = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class AgreementTerminatedEvent(AgreementOperationEvent):
    terminator: Literal["Requestor","Provider"]  # readonly: False
    signature: Optional[str]  # readonly: False
    reason: Reason  # readonly: False

    def __init__(self,
        event_type: str,
        event_date: Timestamp,
        agreement_id: str,
        terminator: Literal["Requestor","Provider"] = None,
        signature: Optional[str] = None,
        reason: Reason = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class AgreementRejectedEventAllOf(AgreementOperationEvent):
    reason: Reason  # readonly: False

    def __init__(self,
        event_type: str,
        event_date: Timestamp,
        agreement_id: str,
        reason: Reason = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class DemandAllOf(DemandOfferBase):
    demand_id: Optional[str]  # readonly: True
    requestor_id: Optional[str]  # readonly: True
    timestamp: Timestamp  # readonly: False

    def __init__(self,
        properties: dict,
        constraints: str,
        demand_id: Optional[str] = None,
        requestor_id: Optional[str] = None,
        timestamp: Timestamp = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class AgreementEvent(Event):
    agreement: Agreement  # readonly: False

    def __init__(self,
        event_type: str,
        event_date: Timestamp,
        agreement: Agreement = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class OfferAllOf(DemandOfferBase):
    offer_id: Optional[str]  # readonly: True
    provider_id: Optional[str]  # readonly: True
    timestamp: Timestamp  # readonly: False

    def __init__(self,
        properties: dict,
        constraints: str,
        offer_id: Optional[str] = None,
        provider_id: Optional[str] = None,
        timestamp: Timestamp = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class Proposal(DemandOfferBase):
    proposal_id: Optional[str]  # readonly: True
    issuer_id: Optional[str]  # readonly: True
    state: Literal["Initial","Draft","Rejected","Accepted","Expired"]  # readonly: True
    timestamp: Timestamp  # readonly: False
    prev_proposal_id: Optional[str]  # readonly: False

    def __init__(self,
        properties: dict,
        constraints: str,
        proposal_id: Optional[str] = None,
        issuer_id: Optional[str] = None,
        state: Literal["Initial","Draft","Rejected","Accepted","Expired"] = None,
        timestamp: Timestamp = None,
        prev_proposal_id: Optional[str] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class ProposalEventAllOf(Event):
    proposal: Proposal  # readonly: False

    def __init__(self,
        event_type: str,
        event_date: Timestamp,
        proposal: Proposal = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class ProposalRejectedEvent(Event):
    proposal_id: Optional[str]  # readonly: True
    reason: Reason  # readonly: False

    def __init__(self,
        event_type: str,
        event_date: Timestamp,
        proposal_id: Optional[str] = None,
        reason: Reason = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class AgreementTerminatedEventAllOf(AgreementOperationEvent):
    terminator: Literal["Requestor","Provider"]  # readonly: False
    signature: Optional[str]  # readonly: False
    reason: Reason  # readonly: False

    def __init__(self,
        event_type: str,
        event_date: Timestamp,
        agreement_id: str,
        terminator: Literal["Requestor","Provider"] = None,
        signature: Optional[str] = None,
        reason: Reason = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class AgreementRejectedEvent(AgreementOperationEvent):
    reason: Reason  # readonly: False

    def __init__(self,
        event_type: str,
        event_date: Timestamp,
        agreement_id: str,
        reason: Reason = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class Demand(DemandOfferBase):
    demand_id: Optional[str]  # readonly: True
    requestor_id: Optional[str]  # readonly: True
    timestamp: Timestamp  # readonly: False

    def __init__(self,
        properties: dict,
        constraints: str,
        demand_id: Optional[str] = None,
        requestor_id: Optional[str] = None,
        timestamp: Timestamp = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class PropertyQueryEventAllOf(Event):
    property_query: PropertyQuery  # readonly: False

    def __init__(self,
        event_type: str,
        event_date: Timestamp,
        property_query: PropertyQuery = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class ProposalAllOf(DemandOfferBase):
    proposal_id: Optional[str]  # readonly: True
    issuer_id: Optional[str]  # readonly: True
    state: Literal["Initial","Draft","Rejected","Accepted","Expired"]  # readonly: True
    timestamp: Timestamp  # readonly: False
    prev_proposal_id: Optional[str]  # readonly: False

    def __init__(self,
        properties: dict,
        constraints: str,
        proposal_id: Optional[str] = None,
        issuer_id: Optional[str] = None,
        state: Literal["Initial","Draft","Rejected","Accepted","Expired"] = None,
        timestamp: Timestamp = None,
        prev_proposal_id: Optional[str] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


