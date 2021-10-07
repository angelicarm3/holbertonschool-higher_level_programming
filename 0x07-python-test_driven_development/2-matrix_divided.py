#!/usr/bin/python3
"""
Funtcion to divide all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divides matrix by div
    Raises:
        TypeError: If the matrix is not a list of lists of int or float
        TypeError: If each row of the matrix doesn't have the same size
        TypeError: If div is not int of float
        ZeroDivisionError: If div = 0
    """
    size = len(matrix[0])
    if len(matrix) == 0 and size == 0 and type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in matrix:
        if len(i) != size:
            raise TypeError("Each row of the matrix must have the same size")
        if type(i) != list:
            raise TypeError("matrix must be a matrix (list of lists) o\
         f integers/floats")
        for j in i:
            if type(j) != int and type(j) != float:
                raise TypeError("matrix must be a matrix (list of lists) o\
         f integers/floats")
    return [[round(num / div, 2) for num in i] for i in matrix]
