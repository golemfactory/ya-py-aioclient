from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from golem_node_api_client.types import UNSET, Unset

if TYPE_CHECKING:
    from golem_node_api_client.models.capture_mode import CaptureMode


T = TypeVar('T', bound='Capture')


@dataclass
class Capture:
    """
    Attributes:
        stdout (Union[Unset, CaptureMode]):
        stderr (Union[Unset, CaptureMode]):
    """

    stdout: Union[Unset, 'CaptureMode'] = UNSET
    stderr: Union[Unset, 'CaptureMode'] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        stdout: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stdout, Unset):
            stdout = self.stdout.to_dict()

        stderr: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stderr, Unset):
            stderr = self.stderr.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stdout is not UNSET:
            field_dict['stdout'] = stdout
        if stderr is not UNSET:
            field_dict['stderr'] = stderr

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from golem_node_api_client.models.capture_mode import CaptureMode

        d = src_dict.copy()
        _stdout = d.pop('stdout', UNSET)
        stdout: Union[Unset, CaptureMode]
        if isinstance(_stdout, Unset):
            stdout = UNSET
        else:
            stdout = CaptureMode.from_dict(_stdout)

        _stderr = d.pop('stderr', UNSET)
        stderr: Union[Unset, CaptureMode]
        if isinstance(_stderr, Unset):
            stderr = UNSET
        else:
            stderr = CaptureMode.from_dict(_stderr)

        capture = cls(
            stdout=stdout,
            stderr=stderr,
        )

        capture.additional_properties = d
        return capture

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
