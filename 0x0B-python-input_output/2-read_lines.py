#!/usr/bin/python3
"""Module 2-read_lines"""


def read_lines(filename="", nb_lines=0):
    """Reads n lines of a text file and prints to stdout"""
    sum_l = 0
    with open(filename) as f:
        for line in f:
            sum_l += 1
    if nb_lines <= 0 or nb_lines >= sum_l:
        nb_lines = sum_l
    with open(filename) as f:
        for i in range(nb_lines):
            print(f.readline(), end="")
