import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.proposal_state import ProposalState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.demand_offer_base_properties import DemandOfferBaseProperties


T = TypeVar("T", bound="Proposal")


@_attrs_define
class Proposal:
    """
    Attributes:
        properties (DemandOfferBaseProperties): The object which includes all the Demand/Offer/Proposal properties.
            This is a JSON object in "flat convention" - where keys are full property names and their values indicate
            properties.

            The value's Javascript type shall conform with the type of the property (as indicated in Golem Standards).
            ### Example property object:
            ```
            {
              "golem.com.pricing.model":"linear",
              "golem.com.pricing.model.linear.coeffs":[0.001, 0.002, 0.0],
              "golem.com.scheme":"payu",
              "golem.com.scheme.payu.interval_sec":6.0,
              "golem.com.usage.vector":["golem.usage.duration_sec","golem.usage.cpu_sec"],
              "golem.inf.cpu.architecture":"x86_64",
              "golem.inf.cpu.cores":4,
              "golem.inf.cpu.threads":7,
              "golem.inf.mem.gib":10.612468048930168,
              "golem.inf.storage.gib":81.7227783203125,
              "golem.node.debug.subnet":"market-devnet",
              "golem.node.id.name":"tworec@mf-market-devnet",
              "golem.runtime.name":"vm",
              "golem.runtime.version@v":"0.1.0"
            }
            ```
        constraints (str):
        proposal_id (str):
        issuer_id (str):
        state (ProposalState): * `Initial` - proposal arrived from the market as response to subscription
            * `Draft` - bespoke counter-proposal issued by one party directly to other party (negotiation phase)
            * `Rejected` by other party
            * `Accepted` - promoted into the Agreement draft
            * `Expired` - not accepted nor rejected before validity period
        timestamp (datetime.datetime):
        prev_proposal_id (Union[Unset, str]): id of the proposal from other side which this proposal responds to
    """

    properties: "DemandOfferBaseProperties"
    constraints: str
    proposal_id: str
    issuer_id: str
    state: ProposalState
    timestamp: datetime.datetime
    prev_proposal_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        properties = self.properties.to_dict()

        constraints = self.constraints

        proposal_id = self.proposal_id

        issuer_id = self.issuer_id

        state = self.state.value

        timestamp = self.timestamp.isoformat()

        prev_proposal_id = self.prev_proposal_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "properties": properties,
                "constraints": constraints,
                "proposalId": proposal_id,
                "issuerId": issuer_id,
                "state": state,
                "timestamp": timestamp,
            }
        )
        if prev_proposal_id is not UNSET:
            field_dict["prevProposalId"] = prev_proposal_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.demand_offer_base_properties import DemandOfferBaseProperties

        d = src_dict.copy()
        properties = DemandOfferBaseProperties.from_dict(d.pop("properties"))

        constraints = d.pop("constraints")

        proposal_id = d.pop("proposalId")

        issuer_id = d.pop("issuerId")

        state = ProposalState(d.pop("state"))

        timestamp = isoparse(d.pop("timestamp"))

        prev_proposal_id = d.pop("prevProposalId", UNSET)

        proposal = cls(
            properties=properties,
            constraints=constraints,
            proposal_id=proposal_id,
            issuer_id=issuer_id,
            state=state,
            timestamp=timestamp,
            prev_proposal_id=prev_proposal_id,
        )

        proposal.additional_properties = d
        return proposal

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
