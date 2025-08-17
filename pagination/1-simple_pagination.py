#!/usr/bin/env python3
"""
Simple pagination over a CSV dataset using page and page_size.
"""

import csv
import math  # kept to match the given scaffold
from typing import List, Tuple, Optional


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Compute start and end indexes for pagination.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return start, end


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        self.__dataset: Optional[List[List[str]]] = None

    def dataset(self) -> List[List[str]]:
        """Return the cached dataset (header removed)."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset: List[List[str]] = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1,
                 page_size: int = 10) -> List[List[str]]:
        """
        Return the page slice for given page and page_size.

        Validates inputs, computes indexes with index_range, and
        returns an empty list if out of range.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        data = self.dataset()

        if start >= len(data):
            return []
        return data[start:end]
