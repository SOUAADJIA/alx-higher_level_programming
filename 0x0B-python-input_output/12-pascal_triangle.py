#!/usr/bin/python3
"""
Module for generating Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Generates the Pascal's triangle of n.

    Args:
        n (int): Number of rows in Pascal's triangle.

    Returns:
        list of list of int: Pascal's triangle represented as a list of
        lists of integers.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # First row of Pascal's triangle
    while len(triangle) < n:
        last_row = triangle[-1]
        new_row = [1]  # First element of each row is always 1

        # Calculate the elements in the current row using the previous row
        for i in range(1, len(last_row)):
            new_row.append(last_row[i - 1] + last_row[i])

        new_row.append(1)  # Last element of each row is always 1
        triangle.append(new_row)

    return triangle
