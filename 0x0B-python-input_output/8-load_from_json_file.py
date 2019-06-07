#!/usr/bin/python3
"""Module 8-load_from_json_file"""
import json


def load_from_json_file(filename):
    """Function creates an object from a json file"""
    with open(filename) as f:
        return json.load(f)
