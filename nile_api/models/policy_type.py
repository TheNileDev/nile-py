from enum import Enum


class PolicyType(str, Enum):
    POLICY = "policy"

    def __str__(self) -> str:
        return str(self.value)
