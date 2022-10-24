from typing import Any, Dict, List, Type, TypeVar, Union
import datetime

from dateutil.parser import isoparse
import attr

from ..models.metadata import Metadata
from ..models.user_org_memberships import UserOrgMemberships
from ..models.user_type import UserType
from ..types import UNSET, Unset

T = TypeVar("T", bound="User")


@attr.s(auto_attribs=True)
class User:
    """
    Attributes:
        type (UserType):
        email (str):
        id (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
        updated (Union[Unset, datetime.datetime]):
        seq (Union[Unset, int]):
        metadata (Union[Unset, Metadata]): Arbitrary metadata. Example: {'location': 'US', 'age': 21, 'active': True,
            'name': {'first': 'John', 'last': 'Doe'}}.
        org_memberships (Union[Unset, UserOrgMemberships]):  Example: {'org_02qaCO8qNEmfpAcomojhLb': {'joined':
            datetime.datetime(2022, 8, 9, 10, 27, 30, 956079), 'metadata': {'region': 'us-east-2'}},
            'org_02qdS9KPAnG6Pt5XFAomu6': {'joined': datetime.datetime(2022, 8, 3, 17, 30, 0, 295581), 'metadata':
            {'region': 'us-west-2'}}}.
    """

    type: UserType
    email: str
    id: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    seq: Union[Unset, int] = UNSET
    metadata: Union[Unset, Metadata] = UNSET
    org_memberships: Union[Unset, UserOrgMemberships] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        email = self.email
        id = self.id
        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        updated: Union[Unset, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        seq = self.seq
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        org_memberships: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.org_memberships, Unset):
            org_memberships = self.org_memberships.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "email": email,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if created is not UNSET:
            field_dict["created"] = created
        if updated is not UNSET:
            field_dict["updated"] = updated
        if seq is not UNSET:
            field_dict["seq"] = seq
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if org_memberships is not UNSET:
            field_dict["org_memberships"] = org_memberships

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = UserType(d.pop("type"))

        email = d.pop("email")

        id = d.pop("id", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _updated = d.pop("updated", UNSET)
        updated: Union[Unset, datetime.datetime]
        if isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = isoparse(_updated)

        seq = d.pop("seq", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, Metadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = Metadata.from_dict(_metadata)

        _org_memberships = d.pop("org_memberships", UNSET)
        org_memberships: Union[Unset, UserOrgMemberships]
        if isinstance(_org_memberships, Unset):
            org_memberships = UNSET
        else:
            org_memberships = UserOrgMemberships.from_dict(_org_memberships)

        user = cls(
            type=type,
            email=email,
            id=id,
            created=created,
            updated=updated,
            seq=seq,
            metadata=metadata,
            org_memberships=org_memberships,
        )

        user.additional_properties = d
        return user

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
