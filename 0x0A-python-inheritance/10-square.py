#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""Module 10-square"""


class Square(Rectangle):
    """Custom class Square inherits Rectangle class"""

    def __init__(self, size):
        """Initialization method for Square class

        Args:
            size: size of square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Function returns area of square"""
        return self.__size ** 2
