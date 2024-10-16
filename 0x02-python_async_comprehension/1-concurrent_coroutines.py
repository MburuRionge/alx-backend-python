#!/usr/bin/env python3
"""Contains an async co-routine"""
import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Return a list of delays"""
    coros = []  # list of coroutines
    delays = []  # list of delays in seconds

    for _ in range(n):
        coros.append(wait_random(max_delay))

    for coro in asyncio.as_completed(coros):
        delays.append(await coro)

    return delays
