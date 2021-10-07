#!/usr/bin/python3
"""
Function to print My name is <First name> <Last Name>
"""


def say_my_name(first_name, last_name=""):
    """
    Prints string
    Raises:
        TypeError: If first_name or last_name are not str
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
