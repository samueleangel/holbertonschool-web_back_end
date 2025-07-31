#!/usr/bin/env python3
"""
This script defines a function that takes a string and a number
(int or float) and returns a tuple. The tuple contains the string
and the square of the number as a float.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string and a number (int or float), and returns a tuple
    where the first element is the string and the second element is
    the square of the number, returned as a float.

    Args:
        k (str): A string key.
        v (Union[int, float]): A number, either int or float.

    Returns:
        Tuple[str, float]: A tuple containing the original string and
        the square of the number (as a float).
    """
    return (k, float(v ** 2))
