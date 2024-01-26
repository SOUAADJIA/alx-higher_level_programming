#!/usr/bin/python3
"""
This module contains the function find_peak(list_of_integers).
"""


def find_peak(lst):
    """
    Find a peak in a list of unsorted integers.
    """
    if not lst:
        return None

    low, high = 0, len(lst) - 1

    while low < high:
        mid = (low + high) // 2
        if lst[mid] > lst[mid + 1]:
            high = mid
        else:
            low = mid + 1

    return lst[low]
