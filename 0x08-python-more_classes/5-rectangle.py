#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return (2 * self.__height) + (2 * self.__width)

    def __str__(self):
        my_str = ''.join(
            ['\n' if i % (self.__width + 1) == 0 else '#' for i in range(
                1, self.__width * self.__height + self.__height)])
        return my_str

    def __repr__(self):
        my_str = "Rectangle(" + str(
            self.__width) + "," + str(self.__height) + ")"
        return my_str

    def __del__(self):
        print("Bye rectangle...")
