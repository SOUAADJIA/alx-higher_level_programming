#!/usr/bin/python3
"""Module for saving objects to JSON files."""

import json


def save_to_json_file(my_obj, filename):
    """
    Save an object to a JSON file.

    Args:
        my_obj (obj): The object to be serialized and saved.
        filename (str): The name of the file to save the JSON data.

    Returns:
        None
    """
    with open(filename, 'w') as json_file:
        json.dump(my_obj, json_file)
