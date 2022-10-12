from enum import Enum


class Action(str, Enum):
    READ = "read"
    WRITE = "write"
    DENY = "deny"

    def __str__(self) -> str:
        return str(self.value)
