import datetime
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from dateutil.parser import isoparse

if TYPE_CHECKING:
    from golem_node_api_client.models.demand_offer_base_properties import DemandOfferBaseProperties


T = TypeVar('T', bound='Offer')


@dataclass
class Offer:
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
        offer_id (str):
        provider_id (str):
        timestamp (datetime.datetime):
    """

    properties: 'DemandOfferBaseProperties'
    constraints: str
    offer_id: str
    provider_id: str
    timestamp: datetime.datetime
    additional_properties: Dict[str, Any] = field(init=False, default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        properties = self.properties.to_dict()

        constraints = self.constraints

        offer_id = self.offer_id

        provider_id = self.provider_id

        timestamp = self.timestamp.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                'properties': properties,
                'constraints': constraints,
                'offerId': offer_id,
                'providerId': provider_id,
                'timestamp': timestamp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from golem_node_api_client.models.demand_offer_base_properties import (
            DemandOfferBaseProperties,
        )

        d = src_dict.copy()
        properties = DemandOfferBaseProperties.from_dict(d.pop('properties'))

        constraints = d.pop('constraints')

        offer_id = d.pop('offerId')

        provider_id = d.pop('providerId')

        timestamp = isoparse(d.pop('timestamp'))

        offer = cls(
            properties=properties,
            constraints=constraints,
            offer_id=offer_id,
            provider_id=provider_id,
            timestamp=timestamp,
        )

        offer.additional_properties = d
        return offer

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
