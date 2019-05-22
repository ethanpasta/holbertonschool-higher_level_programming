#!/usr/bin/python3
class Square:
    """ Square class
    """

    def __init__(self, size=0):
        """ Initialization of square object

        Args:
            size: size of the square
        """
        self.__size = size

    @property
    def size(self):
        """ Getter method for size property
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter method for size property

        Args:
            value: new value of size
        """
        if type(value) is not int:
            raise TypeError('size must be a number')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """ Method returns area of square
        """
        return self.__size ** 2

    def __lt__(self, other):
        """ Method for comparison '<'

        Args:
            other: object to compare to
        """
        return self.__size < other.size

    def __le__(self, other):
        """ Method for comparison '<='

        Args:
            other: object to compare to
        """
        return self.__size <= other.size

    def __eq__(self, other):
        """ Method for comparison '='

        Args:
            other: object to compare to
        """
        return self.__size == other.size

    def __ne__(self, other):
        """ Method for comparison '!='

        Args:
            other: object to compare to
        """
        return self.__size != other.size

    def __gt__(self, other):
        """ Method for comparison '>'

        Args:
            other: object to compare to
        """
        return self.__size > other.size

    def __ge__(self, other):
        """ Method for comparison '>='

        Args:
            other: object to compare to
        """
        return self.__size >= other.size
