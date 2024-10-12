#!/usr/bin/env python3
"""Returns a function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiples
        a string with multiplier"""
    def inner(val: float) -> float:
        """Return product"""
        return val * multiplier

    return inner
