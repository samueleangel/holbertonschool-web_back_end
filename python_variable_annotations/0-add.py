#!/usr/bin/env python3
"""
A script for type-annotated function that makes
the sum of a and b
"""


def add(a: float, b: float) -> float:
    """
    Sum function

    Args:
        a (float): First float value
        b (float): Second float value

    Returns:
        Sum of a + b, returns float
    """
    return a + b
