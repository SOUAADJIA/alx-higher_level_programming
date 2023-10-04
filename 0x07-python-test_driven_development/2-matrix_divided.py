#!/usr/bin/python3
"""
Matrix Division Module

Contains a function matrix_divided that divides all elements of a matrix by 
a given number.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given number.

    Args:
        matrix (list): List of lists containing integers or floats.
        div (int or float): The divisor value.

    Returns:
        list: New matrix with elements divided by div, rounded to 
        2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.
    """
    error_message = 'matrix must be a matrix (list of lists) of integers/floats'

    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError(error_message)

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(error_message)
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(error_message)

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    result_matrix = [row[:] for row in matrix]
    for row_idx in range(len(matrix)):
        for col_idx in range(len(matrix[0])):
            result_matrix[row_idx][col_idx] = round(
                    matrix[row_idx][col_idx] / div, 2)

    return result_matrix
