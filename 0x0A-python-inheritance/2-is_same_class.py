#!/usr/bin/python3
""" Module is_same_class
"""


def is_same_class(obj, a_class):
    """ Function returns true if object is exact instance of a class

    Args:
        obj: the object
        a_class: the class
    """
    return obj.__class__ == a_class
