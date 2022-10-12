from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.error_error_code import ErrorErrorCode

T = TypeVar("T", bound="Error")


@attr.s(auto_attribs=True)
class Error:
    """
    Attributes:
        error_code (ErrorErrorCode):
        message (str):
        status_code (int):
    """

    error_code: ErrorErrorCode
    message: str
    status_code: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error_code = self.error_code.value

        message = self.message
        status_code = self.status_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error_code": error_code,
                "message": message,
                "status_code": status_code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        error_code = ErrorErrorCode(d.pop("error_code"))

        message = d.pop("message")

        status_code = d.pop("status_code")

        error = cls(
            error_code=error_code,
            message=message,
            status_code=status_code,
        )

        error.additional_properties = d
        return error

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
