#!/usr/bin/python3
class Square:
    """ Square class
    """

    def __init__(self, size=0, position=(0, 0)):
        """ Initialization for square object

        Args:
            size: size of square
            position: position to print the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Getter for size property
        """
        return self.__size

    @property
    def position(self):
        """ Getter for position property
        """
        return self.__position

    @size.setter
    def size(self, value):
        """ Setter for size property

        Args:
            value: new size of square
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @position.setter
    def position(self, value):
        """ Setter for position property

        Args:
            value: new position of square
        """
        if type(value) is not tuple or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def my_print(self):
        """ Method to print square to stdout
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(' ' * self.__position[0], end='')
            for j in range(self.__size):
                print('#', end='')
            print()
