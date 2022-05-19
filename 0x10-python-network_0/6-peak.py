#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """ Returns an int (Peak-Max)"""

    if len(list_of_integers) < 1:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]
