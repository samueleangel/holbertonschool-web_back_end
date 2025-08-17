#!/usr/bin/env python3
"""
Module that defines a function to update the topics
of a school document based on its name.
"""

from typing import List
from pymongo.collection import Collection


def update_topics(mongo_collection: Collection,
                  name: str, topics: List[str]) -> None:
    """
    Change all topics of the school document(s)
    matching the given name.

    Args:
        mongo_collection: pymongo collection object.
        name: the school name to match.
        topics: list of topics to set.
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
