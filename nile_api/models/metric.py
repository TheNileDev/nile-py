from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.measurement import Measurement
from ..models.metric_type import MetricType

T = TypeVar("T", bound="Metric")


@attr.s(auto_attribs=True)
class Metric:
    """
    Attributes:
        name (str): The name of the metric that is unique in a workspace
        type (MetricType): Type of metric. Currently sum or gauge
        entity_type (str): The Nile entity type this metric is related to
        measurements (List[Measurement]): Measurements associated with this metric
    """

    name: str
    type: MetricType
    entity_type: str
    measurements: List[Measurement]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        type = self.type.value

        entity_type = self.entity_type
        measurements = []
        for measurements_item_data in self.measurements:
            measurements_item = measurements_item_data.to_dict()

            measurements.append(measurements_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type,
                "entity_type": entity_type,
                "measurements": measurements,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        type = MetricType(d.pop("type"))

        entity_type = d.pop("entity_type")

        measurements = []
        _measurements = d.pop("measurements")
        for measurements_item_data in _measurements:
            measurements_item = Measurement.from_dict(measurements_item_data)

            measurements.append(measurements_item)

        metric = cls(
            name=name,
            type=type,
            entity_type=entity_type,
            measurements=measurements,
        )

        metric.additional_properties = d
        return metric

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
