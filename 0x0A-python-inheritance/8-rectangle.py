#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Module 8-rectangle"""


class Rectangle(BaseGeometry):
    """Custom class Rectangle that inherits BaseGeometry"""

    def __init__(self, width, height):
        """Function initializes object

        Args:
            width: width of rectangle
            height: height of rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
