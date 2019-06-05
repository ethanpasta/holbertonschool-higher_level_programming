#!/usr/bin/python3
"""Module 100-my_int"""


class MyInt(int):
    """Custom class MyInt changes behaviour of integer comparisons"""

    def __eq__(self, other):
        """Function returns false if two objects are equal"""
        return False

    def __ne__(self, other):
        """Function returns true if two objects are not equal"""
        return True
