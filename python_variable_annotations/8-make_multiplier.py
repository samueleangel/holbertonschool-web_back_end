#!/usr/bin/env python3
"""
This script defines a higher-order function that returns
a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The value by which other floats will be multiplied.

    Returns:
        Callable[[float], float]: A function that takes a float and returns
        the result of multiplying it by `multiplier`.
    """
    def multiply(value: float) -> float:
        return value * multiplier

    return multiply
