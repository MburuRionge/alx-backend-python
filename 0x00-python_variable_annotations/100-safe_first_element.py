#!/usr/bin/env python3
"""Contains safe_first_element"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns a sequence or NoneType"""
    if lst:
        return lst[0]
    else:
        return None
