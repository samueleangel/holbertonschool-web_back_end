#!/usr/bin/env python3
"""
This module contains a function with type-annotated
values in it.
"""

from typing import List


def sum_mixed_list(mxd_list: list[int, float]) -> float:
    """
    This function takes a mixed list and returns the sum of the
    items as float:

    Args:
        mxd_list: Value of type list containing ints and floats

    Returns:
        The sum of all the values inside of mxd_list in form of
        float
    """
    return sum(mxd_list)
