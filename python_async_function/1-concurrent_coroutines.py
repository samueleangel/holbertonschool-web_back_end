#!/usr/bin/env python3
"""
This module defines an asynchronous function that runs multiple
coroutines concurrently and returns the delays in ascending order.
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn `n` coroutines of wait_random with the given `max_delay` and return
    a list of the delays in ascending order.

    Args:
        n (int): Number of coroutines to spawn.
        max_delay (int): Maximum delay for each coroutine.

    Returns:
        List[float]: List of delay values in ascending order.
    """
    delays: List[float] = []
    for coroutine in asyncio.as_completed([wait_random(max_delay)
                                           for _ in range(n)]):
        result = await coroutine
        delays.append(result)
    return delays
