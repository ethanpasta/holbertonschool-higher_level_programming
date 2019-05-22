#!/usr/bin/python3
class Square:
    """ Squre class
    """

    def __init__(self, size=0):
        """ Initialization of Square object

        Args:
            size: size of the square
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """ Method to return area of the square
        """
        return self.__size ** 2
