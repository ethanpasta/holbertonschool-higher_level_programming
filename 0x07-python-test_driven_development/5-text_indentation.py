#!/usr/bin/python3
"""
Module for 5-text_indentation
Program prints organized text
"""
def text_indentation(text):
    """ Prints newlines after characters ':' '.' '?'

    Args:
        text: text to iterate through
    """
    if type(text) is not str:
        raise TypeError('text must be a string')
    flag = 0
    for c in text:
        if c == " " and flag == 1:
            flag = 0
            continue
        print(c, end="")
        if c in ".:?":
            flag = 1
            print('\n')
