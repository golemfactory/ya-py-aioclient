from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.property_query_issuer_properties import PropertyQueryIssuerProperties


T = TypeVar("T", bound="PropertyQuery")


@_attrs_define
class PropertyQuery:
    """
    Attributes:
        queried_properties (List[str]):
        issuer_properties (Union[Unset, PropertyQueryIssuerProperties]):
        query_id (Union[Unset, str]):
    """

    queried_properties: List[str]
    issuer_properties: Union[Unset, "PropertyQueryIssuerProperties"] = UNSET
    query_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        queried_properties = self.queried_properties

        issuer_properties: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.issuer_properties, Unset):
            issuer_properties = self.issuer_properties.to_dict()

        query_id = self.query_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "queriedProperties": queried_properties,
            }
        )
        if issuer_properties is not UNSET:
            field_dict["issuerProperties"] = issuer_properties
        if query_id is not UNSET:
            field_dict["queryId"] = query_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.property_query_issuer_properties import (
            PropertyQueryIssuerProperties,
        )

        d = src_dict.copy()
        queried_properties = cast(List[str], d.pop("queriedProperties"))

        _issuer_properties = d.pop("issuerProperties", UNSET)
        issuer_properties: Union[Unset, PropertyQueryIssuerProperties]
        if isinstance(_issuer_properties, Unset):
            issuer_properties = UNSET
        else:
            issuer_properties = PropertyQueryIssuerProperties.from_dict(
                _issuer_properties
            )

        query_id = d.pop("queryId", UNSET)

        property_query = cls(
            queried_properties=queried_properties,
            issuer_properties=issuer_properties,
            query_id=query_id,
        )

        property_query.additional_properties = d
        return property_query

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
