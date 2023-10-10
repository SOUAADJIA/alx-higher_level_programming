#!/usr/bin/python3
"""
Module for appending text after lines containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text after each line containing the specified string.

    Args:
        filename (str): Name of the file to modify.
        search_string (str): String to search for in each line.
        new_string (str): Line of text to insert after each line containing
        the search_string.

    Returns:
        None
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
