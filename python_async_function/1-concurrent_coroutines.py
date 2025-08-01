#!/usr/bin/env python3
"""
This module defines a basic asynchronous coroutine that simulates
a random delay and returns the duration of that delay as a float.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between
    0 and max_delay seconds and returns the delay duration.

    Args:
        max_delay (int): Maximum delay time in seconds. Defaults to 10.

    Returns:
        float: The randomly generated delay duration in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
