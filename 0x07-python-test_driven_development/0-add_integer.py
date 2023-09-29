#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): First number.
        b (int or float, optional): Second number. Defaults to 98.

    Returns:
        int: Sum of a and b.

    Raises:
        TypeError: If a is not an integer or float.
        TypeError: If b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    return int(a) + int(b)
