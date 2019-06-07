#!/usr/bin/python3
"""Module 5-to_json_string"""
import json


def to_json_string(my_obj):
    """Returns json representation of an object"""
    j = json.dumps(my_obj)
    return j
