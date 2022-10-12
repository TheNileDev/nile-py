from enum import Enum


class MetricType(str, Enum):
    GAUGE = "gauge"
    SUM = "sum"

    def __str__(self) -> str:
        return str(self.value)
