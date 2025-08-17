#!/usr/bin/env python3
"""
Module that defines a function to find all schools
that teach a given topic.
"""

from typing import List, Dict
from pymongo.collection import Collection


def schools_by_topic(mongo_collection: Collection,
                     topic: str) -> List[Dict]:
    """
    Return all school documents containing the topic.

    Args:
        mongo_collection: pymongo collection object.
        topic: topic string to search.

    Returns:
        List of matching documents.
    """
    return list(mongo_collection.find({"topics": topic}))
