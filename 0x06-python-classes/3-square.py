#!/usr/bin/python3
"""Create class Square with size"""


class Square:
    """Definition class square"""
    def __init__(self, new_size=0):
        if type(new_size) != int:
            raise TypeError("size must be an integer")
        if new_size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = new_size

        def area(self):
            return self.__size ** 2
