from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.json_schema import JsonSchema

T = TypeVar("T", bound="UpdateEntityRequest")


@attr.s(auto_attribs=True)
class UpdateEntityRequest:
    """
    Attributes:
        schema (JsonSchema): A JSON Schema Example: {'type': 'object', 'properties': {'id': {'type': 'string'},
            'memory': {'type': 'integer'}, 'cpus': {'type': 'integer'}}}.
    """

    schema: JsonSchema
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        schema = self.schema.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "schema": schema,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        schema = JsonSchema.from_dict(d.pop("schema"))

        update_entity_request = cls(
            schema=schema,
        )

        update_entity_request.additional_properties = d
        return update_entity_request

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
