#!/usr/bin/python3
"""
Module matrix_divided
Creates a new matrix with every element divided by a value
"""
def matrix_divided(matrix, div):
    """ Function returns a new matrix with every element divided by 'div'
    """
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if type(matrix) is not list:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    if matrix == [] or matrix == [[]]:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    row_l = len(matrix[0])
    for row in matrix:
        if type(row) is not list:
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        if len(row) != row_l:
            raise TypeError('Each row of the matrix must have the same size')
        for col in row:
            if not isinstance(col, (int, float)):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    return [[round(x / div, 2) for x in row] for row in matrix]
