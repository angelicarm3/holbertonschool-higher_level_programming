#!/usr/bin/python3
"""Create class Square with size"""


class Square:
    """Definition class square"""
    def __init__(self, new_size=0, position=(0, 0)):
        self.__size = new_size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) != int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.size != 0:
            for i in range(self.size):
                print(" " * self.__position[0], end="")
                print("#" * self.size)
        else:
            print("\n" * self.__position[1], end="")
