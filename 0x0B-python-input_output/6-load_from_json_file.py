#!/usr/bin/python3
"""
Module for loading Python objects from JSON files.
"""

import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to be loaded.

    Returns:
        object: The Python object loaded from the JSON file.
    """
    with open(filename, 'r') as file:
        return json.load(file)
