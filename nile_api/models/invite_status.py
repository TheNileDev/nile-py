from enum import Enum


class InviteStatus(str, Enum):
    ACTIVE = "active"

    def __str__(self) -> str:
        return str(self.value)
