from typing import Any, Dict, List, Type, TypeVar
import datetime

from dateutil.parser import isoparse
import attr

T = TypeVar("T", bound="Measurement")


@attr.s(auto_attribs=True)
class Measurement:
    """Measurements associated with this metric

    Attributes:
        timestamp (datetime.datetime): An ISO-8601 formatted date-time, i.e., 2018-11-13T20:20:39+00:00, that represents
            the time the measurement was created. Example: 2022-11-13 20:20:39+00:00.
        value (float): the measured value Example: 11.8.
        instance_id (str): InstanceId of the Nile instance this measurement is related to Example:
            inst_02qwn8bovgrXdNx8XlVzbU.
    """

    timestamp: datetime.datetime
    value: float
    instance_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        timestamp = self.timestamp.isoformat()

        value = self.value
        instance_id = self.instance_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "value": value,
                "instance_id": instance_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        timestamp = isoparse(d.pop("timestamp"))

        value = d.pop("value")

        instance_id = d.pop("instance_id")

        measurement = cls(
            timestamp=timestamp,
            value=value,
            instance_id=instance_id,
        )

        measurement.additional_properties = d
        return measurement

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
