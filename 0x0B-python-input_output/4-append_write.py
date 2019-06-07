#!/usr/bin/python3
"""Module 4-append_write"""


def append_write(filename="", text=""):
    """Appends a string to the end of a text file
    Returns number of characters added
    """
    with open(filename, 'a+') as f:
        return f.write(text)
