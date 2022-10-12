from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.metadata import Metadata
from ..types import UNSET, Unset

T = TypeVar("T", bound="AddUserToOrgRequest")


@attr.s(auto_attribs=True)
class AddUserToOrgRequest:
    """
    Attributes:
        email (str):
        metadata (Union[Unset, Metadata]): Arbitrary metadata. Example: {'location': 'US', 'age': 21, 'active': True,
            'name': {'first': 'John', 'last': 'Doe'}}.
    """

    email: str
    metadata: Union[Unset, Metadata] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email = self.email
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        email = d.pop("email")

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, Metadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = Metadata.from_dict(_metadata)

        add_user_to_org_request = cls(
            email=email,
            metadata=metadata,
        )

        add_user_to_org_request.additional_properties = d
        return add_user_to_org_request

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
