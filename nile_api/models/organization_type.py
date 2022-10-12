from enum import Enum


class OrganizationType(str, Enum):
    NILE = "nile"
    ORGANIZATION = "organization"
    WORKSPACE = "workspace"

    def __str__(self) -> str:
        return str(self.value)
