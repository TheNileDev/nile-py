from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.invite_status import InviteStatus

T = TypeVar("T", bound="Invite")


@attr.s(auto_attribs=True)
class Invite:
    """
    Attributes:
        code (str):
        org (str):
        inviter (str):
        status (InviteStatus):
    """

    code: str
    org: str
    inviter: str
    status: InviteStatus
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code = self.code
        org = self.org
        inviter = self.inviter
        status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "org": org,
                "inviter": inviter,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        code = d.pop("code")

        org = d.pop("org")

        inviter = d.pop("inviter")

        status = InviteStatus(d.pop("status"))

        invite = cls(
            code=code,
            org=org,
            inviter=inviter,
            status=status,
        )

        invite.additional_properties = d
        return invite

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
