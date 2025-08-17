#!/usr/bin/env python3
"""
Module that defines a function to list all documents
from a MongoDB collection.
"""

from typing import List, Dict


def list_all(mongo_collection) -> List[Dict]:
    """
    List all documents in the given collection.

    Args:
        mongo_collection: pymongo collection object.

    Returns:
        A list of documents, or an empty list if none.
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
