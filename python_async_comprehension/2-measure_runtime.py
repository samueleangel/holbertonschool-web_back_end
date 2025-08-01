#!/usr/bin/env python3
"""
This module defines a coroutine that measures the runtime of executing
four async comprehensions concurrently.
"""

import asyncio
import time
from typing import Callable
async_comprehension = __import__(
    '1-async_comprehension'
).async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension 4 times concurrently and measures
    the total runtime.

    Returns:
        float: The total time taken to execute all 4 comprehensions.
    """
    start: float = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end: float = time.time()
    return end - start
