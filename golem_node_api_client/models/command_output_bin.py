from dataclasses import dataclass, field
from io import BytesIO
from typing import Any, Dict, List, Type, TypeVar

from golem_node_api_client.types import File

T = TypeVar('T', bound='CommandOutputBin')


@dataclass
class CommandOutputBin:
    """
    Attributes:
        bin_ (List[File]):
    """

    bin_: List[File]
    additional_properties: Dict[str, Any] = field(init=False, default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bin_ = []
        for bin_item_data in self.bin_:
            bin_item = bin_item_data.to_tuple()

            bin_.append(bin_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                'bin': bin_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        bin_ = []
        _bin_ = d.pop('bin')
        for bin_item_data in _bin_:
            bin_item = File(payload=BytesIO(bin_item_data))

            bin_.append(bin_item)

        command_output_bin = cls(
            bin_=bin_,
        )

        command_output_bin.additional_properties = d
        return command_output_bin

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
