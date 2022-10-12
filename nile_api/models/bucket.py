import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.bucket_bucket_size import BucketBucketSize
from ..types import UNSET, Unset

T = TypeVar("T", bound="Bucket")


@attr.s(auto_attribs=True)
class Bucket:
    """The buckets of the aggregation

    Attributes:
        timestamp (Union[Unset, datetime.datetime]): The timestamp when the bucket starts
        bucket_size (Union[Unset, BucketBucketSize]): The size of the bucket
        average (Union[Unset, float]): The average of all values in the bucket
        sum_ (Union[Unset, float]): The sum of all values in the bucket
        min_ (Union[Unset, float]): The min of all values in the bucket
        max_ (Union[Unset, float]): The max of all values in the bucket
        percentile_95 (Union[Unset, float]): The 95th percentile
    """

    timestamp: Union[Unset, datetime.datetime] = UNSET
    bucket_size: Union[Unset, BucketBucketSize] = UNSET
    average: Union[Unset, float] = UNSET
    sum_: Union[Unset, float] = UNSET
    min_: Union[Unset, float] = UNSET
    max_: Union[Unset, float] = UNSET
    percentile_95: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        bucket_size: Union[Unset, str] = UNSET
        if not isinstance(self.bucket_size, Unset):
            bucket_size = self.bucket_size.value

        average = self.average
        sum_ = self.sum_
        min_ = self.min_
        max_ = self.max_
        percentile_95 = self.percentile_95

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if bucket_size is not UNSET:
            field_dict["bucket_size"] = bucket_size
        if average is not UNSET:
            field_dict["average"] = average
        if sum_ is not UNSET:
            field_dict["sum"] = sum_
        if min_ is not UNSET:
            field_dict["min"] = min_
        if max_ is not UNSET:
            field_dict["max"] = max_
        if percentile_95 is not UNSET:
            field_dict["percentile_95"] = percentile_95

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _timestamp = d.pop("timestamp", UNSET)
        timestamp: Union[Unset, datetime.datetime]
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        _bucket_size = d.pop("bucket_size", UNSET)
        bucket_size: Union[Unset, BucketBucketSize]
        if isinstance(_bucket_size, Unset):
            bucket_size = UNSET
        else:
            bucket_size = BucketBucketSize(_bucket_size)

        average = d.pop("average", UNSET)

        sum_ = d.pop("sum", UNSET)

        min_ = d.pop("min", UNSET)

        max_ = d.pop("max", UNSET)

        percentile_95 = d.pop("percentile_95", UNSET)

        bucket = cls(
            timestamp=timestamp,
            bucket_size=bucket_size,
            average=average,
            sum_=sum_,
            min_=min_,
            max_=max_,
            percentile_95=percentile_95,
        )

        bucket.additional_properties = d
        return bucket

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
