from dataclasses import dataclass, field
from typing import Any, Dict, List, Type, TypeVar, Union

from golem_node_api_client.models.activity_state_state_item import ActivityStateStateItem
from golem_node_api_client.types import UNSET, Unset

T = TypeVar('T', bound='ActivityState')


@dataclass
class ActivityState:
    """
    Attributes:
        state (List[ActivityStateStateItem]): State pair tuple (CurrentState, NextState). NextState is equal to null if
            there is no pending transition between states.
        reason (Union[Unset, str]): Reason for Activity termination (specified when Activity in Terminated state).
        error_message (Union[Unset, str]): If error caused state change - error message shall be provided.
    """

    state: List[ActivityStateStateItem]
    reason: Union[Unset, str] = UNSET
    error_message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        state = []
        for state_item_data in self.state:
            state_item = state_item_data.value
            state.append(state_item)

        reason = self.reason

        error_message = self.error_message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                'state': state,
            }
        )
        if reason is not UNSET:
            field_dict['reason'] = reason
        if error_message is not UNSET:
            field_dict['errorMessage'] = error_message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        state = []
        _state = d.pop('state')
        for state_item_data in _state:
            state_item = ActivityStateStateItem(state_item_data)

            state.append(state_item)

        reason = d.pop('reason', UNSET)

        error_message = d.pop('errorMessage', UNSET)

        activity_state = cls(
            state=state,
            reason=reason,
            error_message=error_message,
        )

        activity_state.additional_properties = d
        return activity_state

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
