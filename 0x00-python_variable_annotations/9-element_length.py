#!/usr/bin/env python3
"""Contains element_length"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns an iterator"""
    return [(i, len(i)) for i in lst]
