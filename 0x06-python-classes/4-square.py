#!/usr/bin/python3
class Square:
    """ Square class
    """

    def __init__(self, size=0):
        """ Initialization of Square object

        Args:
            size: size of square
        """
        self.__size = size

    @property
    def size(self):
        """ Getter for size property
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter for size property

        Args:
            value: new value for size
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """ Method that returns area of square object
        """
        return self.__size ** 2
