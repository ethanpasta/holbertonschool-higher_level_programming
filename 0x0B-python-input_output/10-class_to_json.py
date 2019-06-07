#!/usr/bin/python3
"""Module 10-class_to_json"""


def class_to_json(obj):
    """Returns the dictionary description of an object"""
    return obj.__dict__
