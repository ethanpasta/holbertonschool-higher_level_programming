#!/usr/bin/python3
"""
Module add_integer
Adds two integers
"""
def add_integer(a, b=98):
    """ Function returns the addition of two integers

    Args:
        a: first integer
        b: second integer (default 98)
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    elif not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
