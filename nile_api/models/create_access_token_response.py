from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.access_token_info import AccessTokenInfo
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateAccessTokenResponse")


@attr.s(auto_attribs=True)
class CreateAccessTokenResponse:
    """
    Attributes:
        token (str): The secret key to use for authentication
        token_info (Union[Unset, AccessTokenInfo]):
    """

    token: str
    token_info: Union[Unset, AccessTokenInfo] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        token = self.token
        token_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.token_info, Unset):
            token_info = self.token_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "token": token,
            }
        )
        if token_info is not UNSET:
            field_dict["token_info"] = token_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        token = d.pop("token")

        _token_info = d.pop("token_info", UNSET)
        token_info: Union[Unset, AccessTokenInfo]
        if isinstance(_token_info, Unset):
            token_info = UNSET
        else:
            token_info = AccessTokenInfo.from_dict(_token_info)

        create_access_token_response = cls(
            token=token,
            token_info=token_info,
        )

        create_access_token_response.additional_properties = d
        return create_access_token_response

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
