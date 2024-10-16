#!/usr/bin/env python3
"""Contains async coroutine"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """wait a random time and return same random number"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
