from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.deploy_command_body import DeployCommandBody


T = TypeVar("T", bound="DeployCommand")


@_attrs_define
class DeployCommand:
    """
    Attributes:
        deploy (DeployCommandBody):
    """

    deploy: "DeployCommandBody"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        deploy = self.deploy.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "deploy": deploy,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.deploy_command_body import DeployCommandBody

        d = src_dict.copy()
        deploy = DeployCommandBody.from_dict(d.pop("deploy"))

        deploy_command = cls(
            deploy=deploy,
        )

        deploy_command.additional_properties = d
        return deploy_command

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
