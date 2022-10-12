from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.metadata import Metadata
from ..models.subject_org_membership import SubjectOrgMembership
from ..types import UNSET, Unset

T = TypeVar("T", bound="Subject")


@attr.s(auto_attribs=True)
class Subject:
    """A subset of properties of a user to authorize against.

    You can specify concrete values for subject properties
    or use variables to match a subject property against a resource property.

    An access policy with no resource (which matches all resources)
    and the following subject would allow access to any resource with the same location as the subject:
    ```
    {
      "metadata": {
        "location": ${resource.properties.location}
      }
    }
    ```

      Attributes:
          id (Union[Unset, str]):
          email (Union[Unset, str]):
          metadata (Union[Unset, Metadata]): Arbitrary metadata. Example: {'location': 'US', 'age': 21, 'active': True,
              'name': {'first': 'John', 'last': 'Doe'}}.
          org_membership (Union[Unset, SubjectOrgMembership]):  Example: {'joined': datetime.datetime(2022, 8, 9, 10, 27,
              30, 956079), 'metadata': {'role': 'admin'}}.
    """

    id: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    metadata: Union[Unset, Metadata] = UNSET
    org_membership: Union[Unset, SubjectOrgMembership] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        email = self.email
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        org_membership: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.org_membership, Unset):
            org_membership = self.org_membership.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if email is not UNSET:
            field_dict["email"] = email
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if org_membership is not UNSET:
            field_dict["org_membership"] = org_membership

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        email = d.pop("email", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, Metadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = Metadata.from_dict(_metadata)

        _org_membership = d.pop("org_membership", UNSET)
        org_membership: Union[Unset, SubjectOrgMembership]
        if isinstance(_org_membership, Unset):
            org_membership = UNSET
        else:
            org_membership = SubjectOrgMembership.from_dict(_org_membership)

        subject = cls(
            id=id,
            email=email,
            metadata=metadata,
            org_membership=org_membership,
        )

        subject.additional_properties = d
        return subject

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
