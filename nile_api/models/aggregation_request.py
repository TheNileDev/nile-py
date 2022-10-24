from typing import Any, Dict, List, Type, TypeVar, Union
import datetime

from dateutil.parser import isoparse
import attr

from ..models.aggregation_request_bucket_size import (
    AggregationRequestBucketSize,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AggregationRequest")


@attr.s(auto_attribs=True)
class AggregationRequest:
    """
    Attributes:
        start_time (datetime.datetime): An ISO-8601 formatted date-time, i.e., 2018-11-13T20:20:39+00:00, that the
            aggregation should start at. This time will be truncated based on bucket_size, i.e., if bucket_size is 1h, then
            the start_time will be truncated to the nearest hour.
        bucket_size (Union[Unset, AggregationRequestBucketSize]): The size of the bucket
        buckets (Union[Unset, int]): Number of buckets to return. Defaults to 3 if not provided. Default: 3.
        organization_id (Union[Unset, str]): The Nile organization id to aggregate on
        instance_id (Union[Unset, str]): The optional Nile instance id to aggregate on
    """

    start_time: datetime.datetime
    bucket_size: Union[Unset, AggregationRequestBucketSize] = UNSET
    buckets: Union[Unset, int] = 3
    organization_id: Union[Unset, str] = UNSET
    instance_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        start_time = self.start_time.isoformat()

        bucket_size: Union[Unset, str] = UNSET
        if not isinstance(self.bucket_size, Unset):
            bucket_size = self.bucket_size.value

        buckets = self.buckets
        organization_id = self.organization_id
        instance_id = self.instance_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start_time": start_time,
            }
        )
        if bucket_size is not UNSET:
            field_dict["bucket_size"] = bucket_size
        if buckets is not UNSET:
            field_dict["buckets"] = buckets
        if organization_id is not UNSET:
            field_dict["organization_id"] = organization_id
        if instance_id is not UNSET:
            field_dict["instance_id"] = instance_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        start_time = isoparse(d.pop("start_time"))

        _bucket_size = d.pop("bucket_size", UNSET)
        bucket_size: Union[Unset, AggregationRequestBucketSize]
        if isinstance(_bucket_size, Unset):
            bucket_size = UNSET
        else:
            bucket_size = AggregationRequestBucketSize(_bucket_size)

        buckets = d.pop("buckets", UNSET)

        organization_id = d.pop("organization_id", UNSET)

        instance_id = d.pop("instance_id", UNSET)

        aggregation_request = cls(
            start_time=start_time,
            bucket_size=bucket_size,
            buckets=buckets,
            organization_id=organization_id,
            instance_id=instance_id,
        )

        aggregation_request.additional_properties = d
        return aggregation_request

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
