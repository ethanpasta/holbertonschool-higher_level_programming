#!/usr/bin/python3
""" Module inherits_from
"""


def inherits_from(obj, a_class):
    """ function that returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class)

    Args:
        obj: the object
        a_class: the specified class
    """
    if type(obj) != a_class:
        return issubclass(type(obj), a_class) and isinstance(obj, a_class)
