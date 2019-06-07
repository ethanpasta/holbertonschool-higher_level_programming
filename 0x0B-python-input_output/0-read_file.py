#!/usr/bin/python3
"""Module 0-read_file"""


def read_file(filename=""):
    """Reads a text file and prints to stdout"""
    with open(filename) as f:
        for line in f:
            print(line, end="")
