#!/usr/bin/python3
"""Module base_geometry"""


class BaseGeometry:
    """Custom class BaseGeometry"""

    def area(self):
        """function raises an error"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """function validates a value

        Args:
            name: name to print with exception
            value: value to check
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
