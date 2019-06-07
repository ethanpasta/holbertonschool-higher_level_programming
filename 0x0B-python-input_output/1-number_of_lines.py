#!/usr/bin/python3
"""Module 1-number_of_lines"""


def number_of_lines(filename=""):
    """Returns number of lines of a text file"""
    with open(filename) as f:
        num_l = 0
        for line in f:
            num_l += 1
    return num_l
