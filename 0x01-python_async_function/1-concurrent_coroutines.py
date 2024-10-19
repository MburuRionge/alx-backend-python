#!/usr/bin/env python3
"""a coroutine that returns the list of all delays"""
import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Return a list of ascending delays"""
    coroutine = []
    delays = []

    for _ in range(n):
        coroutine.append(wait_random(max_delay))

    for cors in asyncio.as_completed(coroutine):
        delays.append(await cors)

    return delays
