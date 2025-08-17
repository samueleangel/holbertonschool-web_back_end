#!/usr/bin/env python3
"""
Module that defines a function to find all schools
that teach a given topic.
"""


def schools_by_topic(mongo_collection, topic):
    """ function that returns the list of school
        having a specific topic
    """
    return mongo_collection.find({"topics": topic})
