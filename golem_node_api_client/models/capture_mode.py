from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from golem_node_api_client.types import UNSET, Unset

if TYPE_CHECKING:
    from golem_node_api_client.models.capture_at_end_body import CaptureAtEndBody
    from golem_node_api_client.models.capture_stream_body import CaptureStreamBody


T = TypeVar('T', bound='CaptureMode')


@dataclass
class CaptureMode:
    """
    Attributes:
        at_end (Union[Unset, CaptureAtEndBody]):
        stream (Union[Unset, CaptureStreamBody]):
    """

    at_end: Union[Unset, 'CaptureAtEndBody'] = UNSET
    stream: Union[Unset, 'CaptureStreamBody'] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        at_end: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.at_end, Unset):
            at_end = self.at_end.to_dict()

        stream: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stream, Unset):
            stream = self.stream.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if at_end is not UNSET:
            field_dict['atEnd'] = at_end
        if stream is not UNSET:
            field_dict['stream'] = stream

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from golem_node_api_client.models.capture_at_end_body import CaptureAtEndBody
        from golem_node_api_client.models.capture_stream_body import CaptureStreamBody

        d = src_dict.copy()
        _at_end = d.pop('atEnd', UNSET)
        at_end: Union[Unset, CaptureAtEndBody]
        if isinstance(_at_end, Unset):
            at_end = UNSET
        else:
            at_end = CaptureAtEndBody.from_dict(_at_end)

        _stream = d.pop('stream', UNSET)
        stream: Union[Unset, CaptureStreamBody]
        if isinstance(_stream, Unset):
            stream = UNSET
        else:
            stream = CaptureStreamBody.from_dict(_stream)

        capture_mode = cls(
            at_end=at_end,
            stream=stream,
        )

        capture_mode.additional_properties = d
        return capture_mode

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
