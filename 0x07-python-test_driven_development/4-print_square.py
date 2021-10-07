#!/usr/bin/python3
"""
Function to print a square with the character #
"""


def print_square(size):
    """
    Prints a square
    Raises:
        TypeError: If size is not int
        ValueError: If size is less than 0
        TypeError: If size is a float and less than 0
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
