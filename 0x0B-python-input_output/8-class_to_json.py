#!/usr/bin/python3
"""Module for class_to_json function."""


def class_to_json(obj):
    """
    Converts object attributes to a dictionary for JSON serialization.

    Args:
        obj: An instance of a Class with serializable attributes.

    Returns:
        dict: A dictionary containing serializable attributes of the object.
    """
    json_dict = {}
    attributes = obj.__dict__
    for key, value in attributes.items():
        if isinstance(value, (int, str, list, dict, bool)):
            json_dict[key] = value
    return json_dict
