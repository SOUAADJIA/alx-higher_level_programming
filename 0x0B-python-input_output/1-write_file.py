#!/usr/bin/python3
"""
Module containing a function to write a string to a text file and return
the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8)
    and returns the number of characters written.

    Args:
        filename (str): The name of the file to be written.
        Default is an empty string.
        text (str): The string to be written to the file.
        Default is an empty string.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
