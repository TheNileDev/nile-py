from enum import Enum


class UserType(str, Enum):
    USER = "user"
    DEVELOPER = "developer"
    SERVICE_ACCOUNT = "service_account"
    NILE_EMPLOYEE = "nile_employee"

    def __str__(self) -> str:
        return str(self.value)
