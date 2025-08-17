#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import Any, Dict, List, Optional


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        self.__dataset: Optional[List[List[str]]] = None
        self.__indexed_dataset: Optional[Dict[int, List[str]]] = None

    def dataset(self) -> List[List[str]]:
        """Return the cached dataset (header removed)."""
        if self.__dataset is None:
            with open(
                self.DATA_FILE, newline="", encoding="utf-8"
            ) as f:
                reader = csv.reader(f)
                rows: List[List[str]] = [row for row in reader]
            self.__dataset = rows[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List[str]]:
        """Return a mapping index -> row for deletion resilience."""
        if self.__indexed_dataset is None:
            data = self.dataset()
            # Build full index map (do not truncate).
            self.__indexed_dataset = {i: row for i, row in enumerate(data)}
        return self.__indexed_dataset

    def get_hyper_index(
        self, index: Optional[int] = None, page_size: int = 10
    ) -> Dict[str, Any]:
        """
        Return a deletion-resilient page starting at `index`.

        The page is collected by walking the indexed map from `index`
        and skipping missing keys, until `page_size` items are taken.
        The `next_index` points to the first index after the last item.
        """
        assert isinstance(page_size, int) and page_size > 0

        # Default to 0 if index is None.
        if index is None:
            index = 0
        assert isinstance(index, int) and index >= 0

        index_map = self.indexed_dataset()
        # Validate against the original length, not current count.
        max_base_len = len(self.dataset())
        assert index < max_base_len

        data: List[List[str]] = []
        cur = index

        # Collect up to `page_size` existing rows.
        while len(data) < page_size and cur < max_base_len:
            if cur in index_map:
                data.append(index_map[cur])
            cur += 1

        next_index: Optional[int] = cur if cur < max_base_len else None

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data,
        }
