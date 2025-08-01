#!/usr/bin/env python3
"""
This module defines a coroutine that collects 10 random float values
from an asynchronous generator using async comprehension.
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 float values from async_generator using async
    comprehension and returns them as a list.

    Returns:
        List[float]: A list containing 10 random float values.
    """
    return [value async for value in async_generator()]
