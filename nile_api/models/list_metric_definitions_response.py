from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.metric_definition import MetricDefinition

T = TypeVar("T", bound="ListMetricDefinitionsResponse")


@attr.s(auto_attribs=True)
class ListMetricDefinitionsResponse:
    """
    Attributes:
        metric_definitions (List[MetricDefinition]): The list of metric definitions for a workspace or entity
    """

    metric_definitions: List[MetricDefinition]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        metric_definitions = []
        for metric_definitions_item_data in self.metric_definitions:
            metric_definitions_item = metric_definitions_item_data.to_dict()

            metric_definitions.append(metric_definitions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metric_definitions": metric_definitions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        metric_definitions = []
        _metric_definitions = d.pop("metric_definitions")
        for metric_definitions_item_data in _metric_definitions:
            metric_definitions_item = MetricDefinition.from_dict(
                metric_definitions_item_data
            )

            metric_definitions.append(metric_definitions_item)

        list_metric_definitions_response = cls(
            metric_definitions=metric_definitions,
        )

        list_metric_definitions_response.additional_properties = d
        return list_metric_definitions_response

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
