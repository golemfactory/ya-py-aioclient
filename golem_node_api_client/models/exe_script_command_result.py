import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.exe_script_command_result_result import ExeScriptCommandResultResult
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExeScriptCommandResult")


@_attrs_define
class ExeScriptCommandResult:
    """
    Attributes:
        index (int):
        event_date (datetime.datetime):
        result (ExeScriptCommandResultResult):
        stdout (Union[Unset, str]):
        stderr (Union[Unset, str]):
        message (Union[Unset, str]):
        is_batch_finished (Union[Unset, bool]):
    """

    index: int
    event_date: datetime.datetime
    result: ExeScriptCommandResultResult
    stdout: Union[Unset, str] = UNSET
    stderr: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    is_batch_finished: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        index = self.index

        event_date = self.event_date.isoformat()

        result = self.result.value

        stdout = self.stdout

        stderr = self.stderr

        message = self.message

        is_batch_finished = self.is_batch_finished

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "index": index,
                "eventDate": event_date,
                "result": result,
            }
        )
        if stdout is not UNSET:
            field_dict["stdout"] = stdout
        if stderr is not UNSET:
            field_dict["stderr"] = stderr
        if message is not UNSET:
            field_dict["message"] = message
        if is_batch_finished is not UNSET:
            field_dict["isBatchFinished"] = is_batch_finished

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        index = d.pop("index")

        event_date = isoparse(d.pop("eventDate"))

        result = ExeScriptCommandResultResult(d.pop("result"))

        stdout = d.pop("stdout", UNSET)

        stderr = d.pop("stderr", UNSET)

        message = d.pop("message", UNSET)

        is_batch_finished = d.pop("isBatchFinished", UNSET)

        exe_script_command_result = cls(
            index=index,
            event_date=event_date,
            result=result,
            stdout=stdout,
            stderr=stderr,
            message=message,
            is_batch_finished=is_batch_finished,
        )

        exe_script_command_result.additional_properties = d
        return exe_script_command_result

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
