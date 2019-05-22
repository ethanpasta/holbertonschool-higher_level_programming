#!/usr/bin/python3
class Square:
    """ Square class
    """

    def __init__(self, size=0):
        """ Initialization for square object
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
            value: new size for square
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """ Method to return area of square
        """
        return self.__size ** 2

    def my_print(self):
        """ Method to print square to stdout
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end='')
            print()
