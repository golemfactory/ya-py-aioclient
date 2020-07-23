from typing import Optional, List
from datetime import datetime
from typing_extensions import Literal, Final

class AgreementProposal(object):
    proposal_id: str  # readonly: False
    valid_to: datetime  # readonly: False

    def __init__(self,
        proposal_id: str,
        valid_to: datetime
    ) -> None: ...
    def to_dict(self) -> dict: ...


class PropertyQuery(object):
    issuer_properties: dict  # readonly: False
    query_id: Optional[str]  # readonly: False
    queried_properties: Optional[list]  # readonly: False

    def __init__(self,
        issuer_properties: dict = None,
        query_id: Optional[str] = None,
        queried_properties: Optional[list] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class Agreement(object):
    agreement_id: str  # readonly: False
    demand: Demand  # readonly: False
    offer: Offer  # readonly: False
    valid_to: datetime  # readonly: False
    approved_date: Optional[datetime]  # readonly: False
    state: Literal["Proposal","Pending","Cancelled","Rejected","Approved","Expired","Terminated"]  # readonly: False
    proposed_signature: Optional[str]  # readonly: False
    approved_signature: Optional[str]  # readonly: False
    committed_signature: Optional[str]  # readonly: False

    def __init__(self,
        agreement_id: str,
        demand: Demand,
        offer: Offer,
        valid_to: datetime,
        state: Literal["Proposal","Pending","Cancelled","Rejected","Approved","Expired","Terminated"],
        approved_date: Optional[datetime] = None,
        proposed_signature: Optional[str] = None,
        approved_signature: Optional[str] = None,
        committed_signature: Optional[str] = None
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


class ErrorMessage(object):
    message: Optional[str]  # readonly: False

    def __init__(self,
        message: Optional[str] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class Event(object):
    event_type: str  # readonly: False
    event_date: datetime  # readonly: False

    def __init__(self,
        event_type: str,
        event_date: datetime
    ) -> None: ...
    def to_dict(self) -> dict: ...


class DemandAllOf(DemandOfferBase):
    demand_id: Optional[str]  # readonly: True
    requestor_id: Optional[str]  # readonly: True

    def __init__(self,
        properties: dict,
        constraints: str,
        demand_id: Optional[str] = None,
        requestor_id: Optional[str] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class PropertyQueryEventAllOf(Event):
    property_query: PropertyQuery  # readonly: False

    def __init__(self,
        event_type: str,
        event_date: datetime,
        property_query: PropertyQuery = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class ProposalEvent(Event):
    proposal: Proposal  # readonly: False

    def __init__(self,
        event_type: str,
        event_date: datetime,
        proposal: Proposal = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class AgreementEvent(Event):
    agreement: Agreement  # readonly: False

    def __init__(self,
        event_type: str,
        event_date: datetime,
        agreement: Agreement = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class OfferAllOf(DemandOfferBase):
    offer_id: Optional[str]  # readonly: True
    provider_id: Optional[str]  # readonly: True

    def __init__(self,
        properties: dict,
        constraints: str,
        offer_id: Optional[str] = None,
        provider_id: Optional[str] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class PropertyQueryEvent(Event):
    property_query: PropertyQuery  # readonly: False

    def __init__(self,
        event_type: str,
        event_date: datetime,
        property_query: PropertyQuery = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class ProposalAllOf(DemandOfferBase):
    proposal_id: Optional[str]  # readonly: True
    issuer_id: Optional[str]  # readonly: True
    state: Literal["Initial","Draft","Rejected","Accepted","Expired"]  # readonly: True
    prev_proposal_id: Optional[str]  # readonly: False

    def __init__(self,
        properties: dict,
        constraints: str,
        proposal_id: Optional[str] = None,
        issuer_id: Optional[str] = None,
        state: Literal["Initial","Draft","Rejected","Accepted","Expired"] = None,
        prev_proposal_id: Optional[str] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class ProposalEventAllOf(Event):
    proposal: Proposal  # readonly: False

    def __init__(self,
        event_type: str,
        event_date: datetime,
        proposal: Proposal = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class AgreementEventAllOf(Event):
    agreement: Agreement  # readonly: False

    def __init__(self,
        event_type: str,
        event_date: datetime,
        agreement: Agreement = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class Offer(DemandOfferBase):
    offer_id: Optional[str]  # readonly: True
    provider_id: Optional[str]  # readonly: True

    def __init__(self,
        properties: dict,
        constraints: str,
        offer_id: Optional[str] = None,
        provider_id: Optional[str] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class Proposal(DemandOfferBase):
    proposal_id: Optional[str]  # readonly: True
    issuer_id: Optional[str]  # readonly: True
    state: Literal["Initial","Draft","Rejected","Accepted","Expired"]  # readonly: True
    prev_proposal_id: Optional[str]  # readonly: False

    def __init__(self,
        properties: dict,
        constraints: str,
        proposal_id: Optional[str] = None,
        issuer_id: Optional[str] = None,
        state: Literal["Initial","Draft","Rejected","Accepted","Expired"] = None,
        prev_proposal_id: Optional[str] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class Demand(DemandOfferBase):
    demand_id: Optional[str]  # readonly: True
    requestor_id: Optional[str]  # readonly: True

    def __init__(self,
        properties: dict,
        constraints: str,
        demand_id: Optional[str] = None,
        requestor_id: Optional[str] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


