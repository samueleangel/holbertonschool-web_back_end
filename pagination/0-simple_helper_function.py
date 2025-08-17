#!/usr/bin/env python3
"""
Module that provides the index_range function used for
pagination calculations.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Compute the start and end indexes for pagination.

    Args:
        page (int): page number (1-indexed, must be >= 1).
        page_size (int): number of items per page (must be >= 1).

    Returns:
        Tuple[int, int]: tuple containing start index (inclusive)
        and end index (exclusive) for slicing a list.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return start, end
