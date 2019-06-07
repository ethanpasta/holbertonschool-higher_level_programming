#!/usr/bin/python3
"""Module 5-from_json_string"""
import json


def from_json_string(my_str):
    """Returns object represented by a json string"""
    j = json.loads(my_str)
    return j
