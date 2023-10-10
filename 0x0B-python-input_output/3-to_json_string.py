#!/usr/bin/python3
"""
Module to demonstrate the usage of to_json_string function.
"""


import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj: The object to be serialized to JSON.

    Returns:
        str: The JSON representation of the input object.
    """
    return json.dumps(my_obj)
