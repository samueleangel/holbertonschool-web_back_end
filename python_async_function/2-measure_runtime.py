#!/usr/bin/env python3
"""
This module defines a function that measures the average runtime
of an asynchronous coroutine executed multiple times.
"""

import time
import asyncio
from typing import Callable
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time of wait_n and returns the
    average time per execution.

    Args:
        n (int): Number of times to run the coroutine.
        max_delay (int): Maximum delay per coroutine.

    Returns:
        float: Average execution time per coroutine.
    """
    start: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    end: float = time.time()
    total_time: float = end - start
    return total_time / n
