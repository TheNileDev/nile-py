from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.metric_definition_type import MetricDefinitionType

T = TypeVar("T", bound="MetricDefinition")


@attr.s(auto_attribs=True)
class MetricDefinition:
    """The list of metric definitions for a workspace or entity

    Attributes:
        name (str): The name of the metric
        type (MetricDefinitionType): The type of the metric
        entity_type (str): The entity type of the metric
    """

    name: str
    type: MetricDefinitionType
    entity_type: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        type = self.type.value

        entity_type = self.entity_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type,
                "entity_type": entity_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        type = MetricDefinitionType(d.pop("type"))

        entity_type = d.pop("entity_type")

        metric_definition = cls(
            name=name,
            type=type,
            entity_type=entity_type,
        )

        metric_definition.additional_properties = d
        return metric_definition

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
