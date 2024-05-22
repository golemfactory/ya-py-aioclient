from dataclasses import dataclass, field
from typing import Any, Dict, List, Type, TypeVar, Union

from golem_node_api_client.models.driver_status_property_kind import DriverStatusPropertyKind
from golem_node_api_client.types import UNSET, Unset

T = TypeVar('T', bound='DriverStatusProperty')


@dataclass
class DriverStatusProperty:
    """Individual actionable property of the payment driver status

    Attributes:
        kind (DriverStatusPropertyKind): Determines what property this is. - InsufficientGas -- Driver cannot proceed
            due to missing gas. - InsufficientToken -- Driver cannot proceed due to missing tokens. - InvalidChainId -- A
            transaction can't be processed because its chain-id
              isn't present in the configuration. This hints at a network being removed
              from driver configuration after a transaction on this network has been
              scheduled.
            - CantSign -- Driver cannot sign transactions (locked wallet?). - RpcError -- All configured RPC endpoints are
            failing. - TxStuck -- Transaction was sent to blockchain successfully but cannot
              proceed any further. Likely indicative of too low setting of max fee
              per gas.
        driver (str): Payment driver to which this status property is applicable
        network (Union[Unset, str]): Indicates which chain the problem occurs on. No statuses other than CantSign
            necessarily imply issues on other chains than the one the status property originates from.
            Present for all status properties other than InvalidChainId.
        needed_gas_est (Union[Unset, str]): Estimate total required gas to complete all outstanding transactions.
            Only present for InsufficientGas
        needed_token_est (Union[Unset, str]): Estimate total required token to complete all outstanding transactions.
            Only present for InsufficientToken
        address (Union[Unset, str]): Relates the status event to a specific blockchain address.
            Only present for CantSign, InsufficientGas and InsufficientToken.
        chain_id (Union[Unset, int]): Chain-id that the error relates to.
            Only present for InvalidChainId.
    """

    kind: DriverStatusPropertyKind
    driver: str
    network: Union[Unset, str] = UNSET
    needed_gas_est: Union[Unset, str] = UNSET
    needed_token_est: Union[Unset, str] = UNSET
    address: Union[Unset, str] = UNSET
    chain_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        kind = self.kind.value

        driver = self.driver

        network = self.network

        needed_gas_est = self.needed_gas_est

        needed_token_est = self.needed_token_est

        address = self.address

        chain_id = self.chain_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                'kind': kind,
                'driver': driver,
            }
        )
        if network is not UNSET:
            field_dict['network'] = network
        if needed_gas_est is not UNSET:
            field_dict['neededGasEst'] = needed_gas_est
        if needed_token_est is not UNSET:
            field_dict['neededTokenEst'] = needed_token_est
        if address is not UNSET:
            field_dict['address'] = address
        if chain_id is not UNSET:
            field_dict['chainId'] = chain_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        kind = DriverStatusPropertyKind(d.pop('kind'))

        driver = d.pop('driver')

        network = d.pop('network', UNSET)

        needed_gas_est = d.pop('neededGasEst', UNSET)

        needed_token_est = d.pop('neededTokenEst', UNSET)

        address = d.pop('address', UNSET)

        chain_id = d.pop('chainId', UNSET)

        driver_status_property = cls(
            kind=kind,
            driver=driver,
            network=network,
            needed_gas_est=needed_gas_est,
            needed_token_est=needed_token_est,
            address=address,
            chain_id=chain_id,
        )

        driver_status_property.additional_properties = d
        return driver_status_property

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
