#!/usr/bin/env python3
"""Return sum of list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return list of float"""
    total: float = 0

    for num in input_list:
        total += num

    return total
