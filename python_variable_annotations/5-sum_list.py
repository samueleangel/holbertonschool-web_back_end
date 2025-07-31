#!/usr/bin/env python3
"""
This script holds a function that takes
a list of floats as argument and returns their
sum as float.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    This function takes a list of floats and sums all of them.

    Args:
        input_list (List[float]): List containing float values.

    Returns:
        float: The sum of all float values inside the list.
    """
    return sum(input_list)
