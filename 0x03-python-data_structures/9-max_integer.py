#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    cp_list = my_list.copy()
    cp_list.sort()
    return cp_list[-1]
