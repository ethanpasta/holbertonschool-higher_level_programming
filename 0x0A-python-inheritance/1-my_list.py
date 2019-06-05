#!/usr/bin/python3
""" Module 1-my_list.py
"""


class MyList(list):
    """ Custom class MyList
    """
    def print_sorted(self):
        """ Function prints a sorted list
        """
        print(sorted(self))
