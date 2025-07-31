#!/usr/bin/env python3
"""
This script defines a function that receives an iterable of sequences
and returns a list of tuples. Each tuple contains the original element
and its length.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences (like lists or strings) and returns
    a list of tuples, where each tuple contains the element and its length.

    Args:
        lst (Iterable[Sequence]): An iterable containing sequence elements.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples with each element and
        its length.
    """
    return [(i, len(i)) for i in lst]
