from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.org_membership import OrgMembership

T = TypeVar("T", bound="UserOrgMemberships")


@attr.s(auto_attribs=True)
class UserOrgMemberships:
    """
    Example:
        {'org_02qaCO8qNEmfpAcomojhLb': {'joined': datetime.datetime(2022, 8, 9, 10, 27, 30, 956079), 'metadata':
            {'role': 'admin'}}, 'org_02qdS9KPAnG6Pt5XFAomu6': {'joined': datetime.datetime(2022, 8, 3, 17, 30, 0, 295581),
            'metadata': {'role': 'member'}}}

    """

    additional_properties: Dict[str, OrgMembership] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_org_memberships = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = OrgMembership.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        user_org_memberships.additional_properties = additional_properties
        return user_org_memberships

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> OrgMembership:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: OrgMembership) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
