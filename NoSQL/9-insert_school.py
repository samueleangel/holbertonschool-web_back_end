#!/usr/bin/env python3
"""
Module that defines a function to insert a document
into a MongoDB collection using kwargs.
"""

from typing import Any
from pymongo.collection import Collection


def insert_school(mongo_collection: Collection, **kwargs: Any):
    """
    Insert a new document in the collection.

    Args:
        mongo_collection: pymongo collection object.
        **kwargs: fields to include in the new document.

    Returns:
        The ObjectId of the inserted document.
    """
    res = mongo_collection.insert_one(kwargs)
    return res.inserted_id
