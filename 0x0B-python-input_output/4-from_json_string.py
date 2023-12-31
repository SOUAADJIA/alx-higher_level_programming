#!/usr/bin/python3
"""
Module From JSON string to Object
"""


import json


def from_json_string(my_str):
    """
    Returns the object represented by a JSON string.
    """
    return json.loads(my_str)
