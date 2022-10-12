import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.entity_type import EntityType
from ..models.json_schema import JsonSchema
from ..types import UNSET, Unset

T = TypeVar("T", bound="Entity")


@attr.s(auto_attribs=True)
class Entity:
    """
    Attributes:
        id (str):
        type (EntityType):
        name (str):  Example: clusters.
        schema (JsonSchema): A JSON Schema Example: {'type': 'object', 'properties': {'id': {'type': 'string'},
            'memory': {'type': 'integer'}, 'cpus': {'type': 'integer'}}}.
        created (Union[Unset, datetime.datetime]):
        updated (Union[Unset, datetime.datetime]):
        seq (Union[Unset, int]):
    """

    id: str
    type: EntityType
    name: str
    schema: JsonSchema
    created: Union[Unset, datetime.datetime] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    seq: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        type = self.type.value

        name = self.name
        schema = self.schema.to_dict()

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        updated: Union[Unset, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        seq = self.seq

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type,
                "name": name,
                "schema": schema,
            }
        )
        if created is not UNSET:
            field_dict["created"] = created
        if updated is not UNSET:
            field_dict["updated"] = updated
        if seq is not UNSET:
            field_dict["seq"] = seq

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        type = EntityType(d.pop("type"))

        name = d.pop("name")

        schema = JsonSchema.from_dict(d.pop("schema"))

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

        entity = cls(
            id=id,
            type=type,
            name=name,
            schema=schema,
            created=created,
            updated=updated,
            seq=seq,
        )

        entity.additional_properties = d
        return entity

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
