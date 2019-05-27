#!/usr/bin/python3
"""
Module 100-matrix_mul
Program multiplies two matrices
"""
def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices and returns the new matrix

    Args:
        m_a: first matrix
        m_b: second matrix
    """
    if type(m_a) is not list:
        raise TypeError('m_a must be a list')
    if type(m_b) is not list:
        raise TypeError('m_b must be a list')
    if m_a == [] or m_a == [[]]:
        raise ValueError('m_a can\'t be empty')
    if m_b == [] or m_b == [[]]:
        raise ValueError('m_b can\'t be empty')
    row_l = len(m_a[0])
    for x in m_a:
        if type(x) is not list:
            raise TypeError('m_a must be a list of lists')
        if len(x) != row_l:
            raise TypeError('each row of m_a must should be of the same size')
        for y in x:
            if not isinstance(y, (float, int)):
                raise TypeError('m_a should contain only integers or floats')
    row_l = len(m_b[0])
    for x in m_b:
        if type(x) is not list:
            raise TypeError('m_b must be a list of lists')
        if len(x) != row_l:
            raise TypeError('each row of m_b must should be of the same size')
        for y in x:
            if not isinstance(y, (float, int)):
                raise TypeError('m_b should contain only integers or floats')

    cols_a = 0
    for row in m_a[0]:
        cols_a += 1
    rows_b = 0
    for row in m_b:
        rows_b += 1
    if cols_a != rows_b:
        raise ValueError('m_a and m_b can\'t be multiplied')

    rows_a = len(m_a)
    cols_a = len(m_a[0])
    rows_b = len(m_b)
    cols_b = len(m_b[0])
    result = [[0 for row in range(cols_b)] for col in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += m_a[i][k] * m_b[k][j]
    return result
