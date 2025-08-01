#!/usr/bin/env python3
"""
This module provides a function that returns an asyncio.Task
for a coroutine that waits a random amount of time.
"""

import asyncio
from typing import Any
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio.Task that wraps the coroutine wait_random.

    Args:
        max_delay (int): Maximum delay time for the coroutine.

    Returns:
        asyncio.Task: The asyncio task object wrapping the wait_random
        coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
