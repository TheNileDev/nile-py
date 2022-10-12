from enum import Enum


class EntityType(str, Enum):
    ENTITY = "entity"

    def __str__(self) -> str:
        return str(self.value)
