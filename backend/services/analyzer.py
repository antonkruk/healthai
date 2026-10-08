from typing import Optional
from enum import Enum

class Status(str,Enum):
    LOW = "ниже диапазона"
    NORMAL = "в пределах диапазона"
    HIGH = "выше диапазона"
    UNKNOWN = "нет референсного диапазона"



def evaluate_result(
        value:float,
        reference_min: float | None,
        reference_max:float | None,

)-> Status:
    if reference_min is None or reference_max is None:
        return Status.UNKNOWN

    if reference_min >= reference_max:
        raise ValueError("Нижняя граница должна быть меньше верхней.")

    if value < reference_min:
        return Status.LOW

    if value > reference_max:
        return Status.HIGH

    return Status.NORMAL
def percent_change(previous: float, current: float) -> Optional[float]:
    if previous == 0:
        return None

    return (current - previous) / previous * 100
