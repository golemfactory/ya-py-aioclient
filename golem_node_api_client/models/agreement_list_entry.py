import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AgreementListEntry")


@_attrs_define
class AgreementListEntry:
    """
    Attributes:
        id (str):
        role (str):
        timestamp (Union[Unset, datetime.datetime]):
        approved_date (Union[Unset, datetime.datetime]):
    """

    id: str
    role: str
    timestamp: Union[Unset, datetime.datetime] = UNSET
    approved_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        role = self.role

        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        approved_date: Union[Unset, str] = UNSET
        if not isinstance(self.approved_date, Unset):
            approved_date = self.approved_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "role": role,
            }
        )
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if approved_date is not UNSET:
            field_dict["approvedDate"] = approved_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        role = d.pop("role")

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: Union[Unset, datetime.datetime]
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        _approved_date = d.pop("approvedDate", UNSET)
        approved_date: Union[Unset, datetime.datetime]
        if isinstance(_approved_date, Unset):
            approved_date = UNSET
        else:
            approved_date = isoparse(_approved_date)

        agreement_list_entry = cls(
            id=id,
            role=role,
            timestamp=timestamp,
            approved_date=approved_date,
        )

        agreement_list_entry.additional_properties = d
        return agreement_list_entry

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
