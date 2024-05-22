import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="AgreementProposal")


@_attrs_define
class AgreementProposal:
    """
    Attributes:
        proposal_id (str): id of the proposal to be promoted to the Agreement
        valid_to (datetime.datetime): End of validity period.

            Agreement needs to be approved, rejected or cancelled before this date; otherwise will expire.
    """

    proposal_id: str
    valid_to: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        proposal_id = self.proposal_id

        valid_to = self.valid_to.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "proposalId": proposal_id,
                "validTo": valid_to,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        proposal_id = d.pop("proposalId")

        valid_to = isoparse(d.pop("validTo"))

        agreement_proposal = cls(
            proposal_id=proposal_id,
            valid_to=valid_to,
        )

        agreement_proposal.additional_properties = d
        return agreement_proposal

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
