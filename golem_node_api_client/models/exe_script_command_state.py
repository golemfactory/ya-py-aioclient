from dataclasses import dataclass, field
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from golem_node_api_client.types import UNSET, Unset

T = TypeVar('T', bound='ExeScriptCommandState')


@dataclass
class ExeScriptCommandState:
    """
    Attributes:
        batch_id (str):
        command (str):
        progress (Union[Unset, str]):
        params (Union[Unset, List[str]]):
    """

    batch_id: str
    command: str
    progress: Union[Unset, str] = UNSET
    params: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        batch_id = self.batch_id

        command = self.command

        progress = self.progress

        params: Union[Unset, List[str]] = UNSET
        if not isinstance(self.params, Unset):
            params = self.params

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                'batchId': batch_id,
                'command': command,
            }
        )
        if progress is not UNSET:
            field_dict['progress'] = progress
        if params is not UNSET:
            field_dict['params'] = params

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        batch_id = d.pop('batchId')

        command = d.pop('command')

        progress = d.pop('progress', UNSET)

        params = cast(List[str], d.pop('params', UNSET))

        exe_script_command_state = cls(
            batch_id=batch_id,
            command=command,
            progress=progress,
            params=params,
        )

        exe_script_command_state.additional_properties = d
        return exe_script_command_state

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
