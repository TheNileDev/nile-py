import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.instance import Instance
from ..models.instance_event_event_type import InstanceEventEventType
from ..types import UNSET, Unset

T = TypeVar("T", bound="InstanceEvent")


@attr.s(auto_attribs=True)
class InstanceEvent:
    """
    Attributes:
        timestamp (datetime.datetime):
        id (Union[Unset, int]):
        event_type (Union[Unset, InstanceEventEventType]):
        before (Union[Unset, Instance]):
        after (Union[Unset, Instance]):
    """

    timestamp: datetime.datetime
    id: Union[Unset, int] = UNSET
    event_type: Union[Unset, InstanceEventEventType] = UNSET
    before: Union[Unset, Instance] = UNSET
    after: Union[Unset, Instance] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        timestamp = self.timestamp.isoformat()

        id = self.id
        event_type: Union[Unset, str] = UNSET
        if not isinstance(self.event_type, Unset):
            event_type = self.event_type.value

        before: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.before, Unset):
            before = self.before.to_dict()

        after: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.after, Unset):
            after = self.after.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if event_type is not UNSET:
            field_dict["event_type"] = event_type
        if before is not UNSET:
            field_dict["before"] = before
        if after is not UNSET:
            field_dict["after"] = after

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        timestamp = isoparse(d.pop("timestamp"))

        id = d.pop("id", UNSET)

        _event_type = d.pop("event_type", UNSET)
        event_type: Union[Unset, InstanceEventEventType]
        if isinstance(_event_type, Unset):
            event_type = UNSET
        else:
            event_type = InstanceEventEventType(_event_type)

        _before = d.pop("before", UNSET)
        before: Union[Unset, Instance]
        if isinstance(_before, Unset):
            before = UNSET
        else:
            before = Instance.from_dict(_before)

        _after = d.pop("after", UNSET)
        after: Union[Unset, Instance]
        if isinstance(_after, Unset):
            after = UNSET
        else:
            after = Instance.from_dict(_after)

        instance_event = cls(
            timestamp=timestamp,
            id=id,
            event_type=event_type,
            before=before,
            after=after,
        )

        instance_event.additional_properties = d
        return instance_event

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
