#!/usr/bin/python3
""" Module is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """ function returns true if object is an instance of, or
    if the object is an instance of a class that inherited from the class

    Args:
        obj: the object
        a_class: the specified class
    """
    return issubclass(type(obj), a_class)
