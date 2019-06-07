#!/usr/bin/python3
"""Module 7-save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """Function writes an object to a text file using
    json representation
    """
    with open(filename, 'w+') as f:
        json.dump(my_obj, f)
