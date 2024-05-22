import datetime
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from dateutil.parser import isoparse

if TYPE_CHECKING:
    from golem_node_api_client.models.proposal import Proposal


T = TypeVar('T', bound='ProposalEvent')


@dataclass
class ProposalEvent:
    """
    Attributes:
        event_type (str):
        event_date (datetime.datetime):
        proposal (Proposal):
    """

    event_type: str
    event_date: datetime.datetime
    proposal: 'Proposal'
    additional_properties: Dict[str, Any] = field(init=False, default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        event_type = self.event_type

        event_date = self.event_date.isoformat()

        proposal = self.proposal.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                'eventType': event_type,
                'eventDate': event_date,
                'proposal': proposal,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from golem_node_api_client.models.proposal import Proposal

        d = src_dict.copy()
        event_type = d.pop('eventType')

        event_date = isoparse(d.pop('eventDate'))

        proposal = Proposal.from_dict(d.pop('proposal'))

        proposal_event = cls(
            event_type=event_type,
            event_date=event_date,
            proposal=proposal,
        )

        proposal_event.additional_properties = d
        return proposal_event

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
