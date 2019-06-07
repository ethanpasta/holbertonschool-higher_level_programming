#!/usr/bin/python3
"""Module 14-pascal_triangle"""


def pascal_triangle(n):
    """Returns list of lists of integers representing a pascal triangle
    of size n
    """
    if (n <= 0):
        return []
    first = [0, 1, 0]
    big_l = [[1]]
    size = 4
    for i in range(n - 1):
        curr = [0] * size
        for j in range(1, size - 1):
            curr[j] = first[j - 1] + first[j]
        big_l.append(curr[1:-1])
        first = curr
        size += 1
    return big_l
