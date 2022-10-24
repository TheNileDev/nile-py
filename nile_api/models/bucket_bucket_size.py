from enum import Enum


class BucketBucketSize(str, Enum):
    VALUE_0 = "1h"
    VALUE_1 = "1d"
    VALUE_2 = "10m"

    def __str__(self) -> str:
        return str(self.value)
