from enum import Enum


class WorkspaceType(str, Enum):
    WORKSPACE = "workspace"

    def __str__(self) -> str:
        return str(self.value)
