#!/usr/bin/env python3
"""Measures the time taken for a function to execute"""
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures time taken to run coroutines"""
    start_time = time.time()

    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()

    return (start_time - end_time)/n
