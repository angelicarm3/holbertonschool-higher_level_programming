#!/usr/bin/python3
"""
Function checks if the object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is an instance of the specified class
    Otherwise returns False
    """
    if type(obj) == a_class:
        return True
    return False
