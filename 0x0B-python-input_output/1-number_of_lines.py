#!/usr/bin/python3
def number_of_lines(filename=""):
    with open(filename) as f:
        num_l = 0
        for line in f:
            num_l += 1
    return num_l
