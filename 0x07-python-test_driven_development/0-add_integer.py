#!/usr/bin/python3
"""
Funtcion to add 2 integers or floats
"""


def add_integer(a, b=98):
    """
    Adds integers a and b
    Raises:
        TypeError: If a or b are not int or float
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    return int(a + b)
