#!/usr/bin/env python3
"""Return sum of list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return sum numbers in mxd_lst"""
    total: float = 0.00

    for num in mxd_lst:
        total += num

    return total
