from typing import Any, Dict, List, Type, TypeVar, Union
import datetime

from dateutil.parser import isoparse
import attr

from ..models.access_token_info_metadata import AccessTokenInfoMetadata
from ..types import UNSET, Unset

T = TypeVar("T", bound="AccessTokenInfo")


@attr.s(auto_attribs=True)
class AccessTokenInfo:
    """
    Attributes:
        id (str):
        label (str): The human-friendly label of the access token
        description (Union[Unset, str]): The intended use of the token
        metadata (Union[Unset, AccessTokenInfoMetadata]): Arbitrary metadata. Example: {'location': 'US', 'age': 21,
            'active': True, 'name': {'first': 'John', 'last': 'Doe'}}.
        created (Union[Unset, datetime.datetime]):
    """

    id: str
    label: str
    description: Union[Unset, str] = UNSET
    metadata: Union[Unset, AccessTokenInfoMetadata] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        label = self.label
        description = self.description
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "label": label,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if created is not UNSET:
            field_dict["created"] = created

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        label = d.pop("label")

        description = d.pop("description", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, AccessTokenInfoMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = AccessTokenInfoMetadata.from_dict(_metadata)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        access_token_info = cls(
            id=id,
            label=label,
            description=description,
            metadata=metadata,
            created=created,
        )

        access_token_info.additional_properties = d
        return access_token_info

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
