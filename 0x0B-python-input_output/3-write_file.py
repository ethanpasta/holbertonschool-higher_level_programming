#!/usr/bin/python3
"""Module 3-write_file"""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns number
    of characters written"""
    with open(filename, 'w+') as f:
        return f.write(text)
