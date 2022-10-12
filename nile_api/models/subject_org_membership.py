import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.metadata import Metadata
from ..types import UNSET, Unset

T = TypeVar("T", bound="SubjectOrgMembership")


@attr.s(auto_attribs=True)
class SubjectOrgMembership:
    """
    Example:
        {'joined': datetime.datetime(2022, 8, 9, 10, 27, 30, 956079), 'metadata': {'role': 'admin'}}

    Attributes:
        joined (Union[Unset, datetime.datetime]):
        metadata (Union[Unset, Metadata]): Arbitrary metadata. Example: {'location': 'US', 'age': 21, 'active': True,
            'name': {'first': 'John', 'last': 'Doe'}}.
    """

    joined: Union[Unset, datetime.datetime] = UNSET
    metadata: Union[Unset, Metadata] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        joined: Union[Unset, str] = UNSET
        if not isinstance(self.joined, Unset):
            joined = self.joined.isoformat()

        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if joined is not UNSET:
            field_dict["joined"] = joined
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _joined = d.pop("joined", UNSET)
        joined: Union[Unset, datetime.datetime]
        if isinstance(_joined, Unset):
            joined = UNSET
        else:
            joined = isoparse(_joined)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, Metadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = Metadata.from_dict(_metadata)

        subject_org_membership = cls(
            joined=joined,
            metadata=metadata,
        )

        subject_org_membership.additional_properties = d
        return subject_org_membership

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
