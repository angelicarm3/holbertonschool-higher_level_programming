#!/usr/bin/python3

"""Function that returns a list of lists of integers"""


def pascal_triangle(n):
    """Representing the Pascal’s triangle of n"""
    if n <= 0:
        return []

    base = [[1]]
    while len(base) != n:
        tri = base[-1]
        temp = [1]
        for i in range(len(tri) - 1):
            temp.append(tri[i] + tri[i + 1])
        temp.append(1)
        base.append(temp)
    return base
