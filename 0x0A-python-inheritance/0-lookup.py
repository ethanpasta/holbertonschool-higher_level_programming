#!/usr/bin/python3
"""
Module 0-lookup.py
"""


def lookup(obj):
    """
    Function returns list of available attributes and methods
    of an object

    Args:
        obj: object
    """
    return dir(obj)
