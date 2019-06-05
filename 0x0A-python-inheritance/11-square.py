#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""Module 11-square"""


class Square(Rectangle):
    """Custom class Square inherits Rectangle"""

    def __init__(self, size):
        """Initialization function for Square class

        Args:
            size: size of the square
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Function returns area of square"""
        return self.__size ** 2

    def __str__(self):
        """Function returns readable representation of a Square object"""
        return "[Square] {}/{}".format(self.__size, self.__size)
