#!/usr/bin/python3

"""
Class MyList that inherits from list
"""


class MyList(list):
    """Class MyList that inherits from list"""

    def print_sorted(self):
        """Prints an ascending sorted list"""
        print(sorted(self))
