from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from golem_node_api_client.types import UNSET, Unset

if TYPE_CHECKING:
    from golem_node_api_client.models.deploy_command_body_hosts import DeployCommandBodyHosts
    from golem_node_api_client.models.deploy_command_body_nodes import DeployCommandBodyNodes
    from golem_node_api_client.models.deploy_network import DeployNetwork


T = TypeVar('T', bound='DeployCommandBody')


@dataclass
class DeployCommandBody:
    """
    Attributes:
        net (Union[Unset, List['DeployNetwork']]):
        hosts (Union[Unset, DeployCommandBodyHosts]):
        nodes (Union[Unset, DeployCommandBodyNodes]):
    """

    net: Union[Unset, List['DeployNetwork']] = UNSET
    hosts: Union[Unset, 'DeployCommandBodyHosts'] = UNSET
    nodes: Union[Unset, 'DeployCommandBodyNodes'] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        net: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.net, Unset):
            net = []
            for net_item_data in self.net:
                net_item = net_item_data.to_dict()
                net.append(net_item)

        hosts: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.hosts, Unset):
            hosts = self.hosts.to_dict()

        nodes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.nodes, Unset):
            nodes = self.nodes.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if net is not UNSET:
            field_dict['net'] = net
        if hosts is not UNSET:
            field_dict['hosts'] = hosts
        if nodes is not UNSET:
            field_dict['nodes'] = nodes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from golem_node_api_client.models.deploy_command_body_hosts import DeployCommandBodyHosts
        from golem_node_api_client.models.deploy_command_body_nodes import DeployCommandBodyNodes
        from golem_node_api_client.models.deploy_network import DeployNetwork

        d = src_dict.copy()
        net = []
        _net = d.pop('net', UNSET)
        for net_item_data in _net or []:
            net_item = DeployNetwork.from_dict(net_item_data)

            net.append(net_item)

        _hosts = d.pop('hosts', UNSET)
        hosts: Union[Unset, DeployCommandBodyHosts]
        if isinstance(_hosts, Unset):
            hosts = UNSET
        else:
            hosts = DeployCommandBodyHosts.from_dict(_hosts)

        _nodes = d.pop('nodes', UNSET)
        nodes: Union[Unset, DeployCommandBodyNodes]
        if isinstance(_nodes, Unset):
            nodes = UNSET
        else:
            nodes = DeployCommandBodyNodes.from_dict(_nodes)

        deploy_command_body = cls(
            net=net,
            hosts=hosts,
            nodes=nodes,
        )

        deploy_command_body.additional_properties = d
        return deploy_command_body

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
