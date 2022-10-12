from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Resource")


@attr.s(auto_attribs=True)
class Resource:
    """A subset of properties of any custom or built-in entity instance to authorize against.

    All properties on a resource are optional, and any combination of them can be specified when creating a policy.
    You can specify concrete values for resource and subject properties
    or use variables to match a subject property against a resource property.

    An access policy with the following resource would allow access to clusters with location matching the subject's
    region:
    ```
    {
      "type": "cluster",
      "properties": {
        "location": ${subject.metadata.location}
      }
    }
    ```


    Note that:
    * Only exact matching of properties is supported for now.
    * For built-in entity instances, only the Policy entity is currently supported.
    * Custom properties on a resource must be specified under the "properties" key.

        Example:
            {'id': 'inst_123', 'type': 'cluster', 'properties': {'region': 'us-west-2', 'status': 'running'}}

        Attributes:
            id (Union[Unset, str]):
            type (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        type = d.pop("type", UNSET)

        resource = cls(
            id=id,
            type=type,
        )

        resource.additional_properties = d
        return resource

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
