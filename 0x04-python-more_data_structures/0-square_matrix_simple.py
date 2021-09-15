#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [list(map(lambda i: i**2, j)) for j in matrix]
    return (new_matrix)
