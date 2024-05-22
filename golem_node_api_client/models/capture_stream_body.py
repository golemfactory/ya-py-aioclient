from dataclasses import dataclass, field
from typing import Any, Dict, List, Type, TypeVar, Union

from golem_node_api_client.models.capture_format import CaptureFormat
from golem_node_api_client.types import UNSET, Unset

T = TypeVar('T', bound='CaptureStreamBody')


@dataclass
class CaptureStreamBody:
    """
    Attributes:
        limit (Union[Unset, float]):
        format_ (Union[Unset, CaptureFormat]):
    """

    limit: Union[Unset, float] = UNSET
    format_: Union[Unset, CaptureFormat] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        limit = self.limit

        format_: Union[Unset, str] = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if limit is not UNSET:
            field_dict['limit'] = limit
        if format_ is not UNSET:
            field_dict['format'] = format_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        limit = d.pop('limit', UNSET)

        _format_ = d.pop('format', UNSET)
        format_: Union[Unset, CaptureFormat]
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = CaptureFormat(_format_)

        capture_stream_body = cls(
            limit=limit,
            format_=format_,
        )

        capture_stream_body.additional_properties = d
        return capture_stream_body

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
