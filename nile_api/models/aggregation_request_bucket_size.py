from enum import Enum


class AggregationRequestBucketSize(str, Enum):
    VALUE_0 = "1h"
    VALUE_1 = "1d"

    def __str__(self) -> str:
        return str(self.value)
