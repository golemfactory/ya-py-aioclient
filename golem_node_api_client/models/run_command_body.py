from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from golem_node_api_client.types import UNSET, Unset

if TYPE_CHECKING:
    from golem_node_api_client.models.capture import Capture


T = TypeVar('T', bound='RunCommandBody')


@dataclass
class RunCommandBody:
    """
    Attributes:
        entry_point (str):
        args (Union[Unset, List[str]]):
        capture (Union[Unset, Capture]):
    """

    entry_point: str
    args: Union[Unset, List[str]] = UNSET
    capture: Union[Unset, 'Capture'] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entry_point = self.entry_point

        args: Union[Unset, List[str]] = UNSET
        if not isinstance(self.args, Unset):
            args = self.args

        capture: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.capture, Unset):
            capture = self.capture.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                'entry_point': entry_point,
            }
        )
        if args is not UNSET:
            field_dict['args'] = args
        if capture is not UNSET:
            field_dict['capture'] = capture

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from golem_node_api_client.models.capture import Capture

        d = src_dict.copy()
        entry_point = d.pop('entry_point')

        args = cast(List[str], d.pop('args', UNSET))

        _capture = d.pop('capture', UNSET)
        capture: Union[Unset, Capture]
        if isinstance(_capture, Unset):
            capture = UNSET
        else:
            capture = Capture.from_dict(_capture)

        run_command_body = cls(
            entry_point=entry_point,
            args=args,
            capture=capture,
        )

        run_command_body.additional_properties = d
        return run_command_body

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
