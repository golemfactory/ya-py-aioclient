from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from golem_node_api_client.types import UNSET, Unset

if TYPE_CHECKING:
    from golem_node_api_client.models.file_set import FileSet


T = TypeVar('T', bound='TransferCommandBody')


@dataclass
class TransferCommandBody:
    """
    Attributes:
        from_ (str):
        to (str):
        format_ (Union[Unset, str]):
        depth (Union[Unset, float]):
        fileset (Union[Unset, List['FileSet']]):
    """

    from_: str
    to: str
    format_: Union[Unset, str] = UNSET
    depth: Union[Unset, float] = UNSET
    fileset: Union[Unset, List['FileSet']] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from_ = self.from_

        to = self.to

        format_ = self.format_

        depth = self.depth

        fileset: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.fileset, Unset):
            fileset = []
            for fileset_item_data in self.fileset:
                fileset_item = fileset_item_data.to_dict()
                fileset.append(fileset_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                'from': from_,
                'to': to,
            }
        )
        if format_ is not UNSET:
            field_dict['format'] = format_
        if depth is not UNSET:
            field_dict['depth'] = depth
        if fileset is not UNSET:
            field_dict['fileset'] = fileset

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from golem_node_api_client.models.file_set import FileSet

        d = src_dict.copy()
        from_ = d.pop('from')

        to = d.pop('to')

        format_ = d.pop('format', UNSET)

        depth = d.pop('depth', UNSET)

        fileset = []
        _fileset = d.pop('fileset', UNSET)
        for fileset_item_data in _fileset or []:
            fileset_item = FileSet.from_dict(fileset_item_data)

            fileset.append(fileset_item)

        transfer_command_body = cls(
            from_=from_,
            to=to,
            format_=format_,
            depth=depth,
            fileset=fileset,
        )

        transfer_command_body.additional_properties = d
        return transfer_command_body

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
