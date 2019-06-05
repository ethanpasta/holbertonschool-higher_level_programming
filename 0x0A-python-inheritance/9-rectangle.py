#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Module 9-rectangle"""


class Rectangle(BaseGeometry):
    """Rectangle class inherits BaseGeometry class"""

    def __init__(self, width, height):
        """Initialization function

        Args:
            width: width of rectangle
            height: height of rectangle
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Function returns area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Function returns human-readable formatted string of a rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
