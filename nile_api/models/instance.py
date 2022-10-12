import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.json_schema_instance import JsonSchemaInstance
from ..types import UNSET, Unset

T = TypeVar("T", bound="Instance")


@attr.s(auto_attribs=True)
class Instance:
    """
    Attributes:
        id (str):
        type (str): The entity type of this instance Example: clusters.
        properties (JsonSchemaInstance): An *instance* of a JSON Schema Example: {'id': 'lkc-123', 'memory': 4096,
            'cpus': 4}.
        created (Union[Unset, datetime.datetime]):
        updated (Union[Unset, datetime.datetime]):
        seq (Union[Unset, int]):
        deleted (Union[Unset, datetime.datetime]):
    """

    id: str
    type: str
    properties: JsonSchemaInstance
    created: Union[Unset, datetime.datetime] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    seq: Union[Unset, int] = UNSET
    deleted: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        type = self.type
        properties = self.properties.to_dict()

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        updated: Union[Unset, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        seq = self.seq
        deleted: Union[Unset, str] = UNSET
        if not isinstance(self.deleted, Unset):
            deleted = self.deleted.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type,
                "properties": properties,
            }
        )
        if created is not UNSET:
            field_dict["created"] = created
        if updated is not UNSET:
            field_dict["updated"] = updated
        if seq is not UNSET:
            field_dict["seq"] = seq
        if deleted is not UNSET:
            field_dict["deleted"] = deleted

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        type = d.pop("type")

        properties = JsonSchemaInstance.from_dict(d.pop("properties"))

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _updated = d.pop("updated", UNSET)
        updated: Union[Unset, datetime.datetime]
        if isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = isoparse(_updated)

        seq = d.pop("seq", UNSET)

        _deleted = d.pop("deleted", UNSET)
        deleted: Union[Unset, datetime.datetime]
        if isinstance(_deleted, Unset):
            deleted = UNSET
        else:
            deleted = isoparse(_deleted)

        instance = cls(
            id=id,
            type=type,
            properties=properties,
            created=created,
            updated=updated,
            seq=seq,
            deleted=deleted,
        )

        instance.additional_properties = d
        return instance

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
