from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, cast

if TYPE_CHECKING:
    from golem_node_api_client.models.market_property import MarketProperty


T = TypeVar('T', bound='MarketDecoration')


@dataclass
class MarketDecoration:
    """Properties and constraints to be added to a market object (i.e. a demand or an offer).

    Attributes:
        properties (List['MarketProperty']):
        constraints (List[str]):
    """

    properties: List['MarketProperty']
    constraints: List[str]
    additional_properties: Dict[str, Any] = field(init=False, default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        properties = []
        for properties_item_data in self.properties:
            properties_item = properties_item_data.to_dict()
            properties.append(properties_item)

        constraints = self.constraints

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                'properties': properties,
                'constraints': constraints,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from golem_node_api_client.models.market_property import MarketProperty

        d = src_dict.copy()
        properties = []
        _properties = d.pop('properties')
        for properties_item_data in _properties:
            properties_item = MarketProperty.from_dict(properties_item_data)

            properties.append(properties_item)

        constraints = cast(List[str], d.pop('constraints'))

        market_decoration = cls(
            properties=properties,
            constraints=constraints,
        )

        market_decoration.additional_properties = d
        return market_decoration

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
