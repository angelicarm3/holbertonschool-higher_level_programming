#!/usr/bin/python3
"""
Function checks if the object is an instance of a class that
inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class
    Otherwise False
    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    return False
