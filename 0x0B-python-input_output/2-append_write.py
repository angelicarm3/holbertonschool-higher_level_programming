#!/usr/bin/python3

"""Function that appends a string at the end of a text file (UTF8)"""
"""the number of characters written"""


def append_write(filename="", text=""):
    """Write a string to a UTF8 text file"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
