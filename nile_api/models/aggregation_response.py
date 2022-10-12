from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.bucket import Bucket
from ..types import UNSET, Unset

T = TypeVar("T", bound="AggregationResponse")


@attr.s(auto_attribs=True)
class AggregationResponse:
    """
    Attributes:
        buckets (Union[Unset, List[Bucket]]): The buckets of the aggregation
    """

    buckets: Union[Unset, List[Bucket]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        buckets: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.buckets, Unset):
            buckets = []
            for buckets_item_data in self.buckets:
                buckets_item = buckets_item_data.to_dict()

                buckets.append(buckets_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if buckets is not UNSET:
            field_dict["buckets"] = buckets

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        buckets = []
        _buckets = d.pop("buckets", UNSET)
        for buckets_item_data in _buckets or []:
            buckets_item = Bucket.from_dict(buckets_item_data)

            buckets.append(buckets_item)

        aggregation_response = cls(
            buckets=buckets,
        )

        aggregation_response.additional_properties = d
        return aggregation_response

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
