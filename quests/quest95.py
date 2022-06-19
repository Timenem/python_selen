
from typing import Tuple


def sum_by_types(items: list) -> Tuple[str, int]:
    integers = 0
    chars = ""
    if len(items) != 0:
        for i in items:
            if isinstance(i, int):
                integers += i
            elif isinstance(i, str):
                chars += i
        return (integers,chars)
    else:
        return (integers,chars)

