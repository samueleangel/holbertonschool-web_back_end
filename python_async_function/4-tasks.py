#!/usr/bin/env python3
"""
This module defines a coroutine that runs multiple task coroutines
concurrently and returns the delays in ascending order.
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns `n` task_wait_random coroutines and returns the list
    of delays in ascending order.

    Args:
        n (int): Number of concurrent tasks to run.
        max_delay (int): Maximum delay for each task.

    Returns:
        List[float]: List of delays in ascending order.
    """
    tasks: List[asyncio.Task] = [
        task_wait_random(max_delay) for _ in range(n)
    ]

    delays: List[float] = []
    for coroutine in asyncio.as_completed(tasks):
        delay = await coroutine
        delays.append(delay)

    return delays
