#!/usr/bin/python3
"""Module rectangle"""
from models.base import Base


class Rectangle(Base):
    """Custom class Rectangle - inherits Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization method for Rectangle instance

        Args:
            width: width
            height: height
            x: x
            y: y
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @width.setter
    def width(self, value):
        """Setter for width

        Args:
            value: new value
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter for height

        Args:
            value: new value
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @x.setter
    def x(self, value):
        """Setter for x

        Args:
            value: new value
        """
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @y.setter
    def y(self, value):
        """Setter for y

        Args:
            value: new value
        """
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """Public method that returns area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """Public method that prints in stdout the rectange"""
        print('\n' * self.__y, end="")
        for x in range(self.__height):
            print(' ' * self.__x, end="")
            for y in range(self.__width):
                print('#', end="")
            print()

    def __str__(self):
        """Public method that returns string represention of rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Public method updates attributes

        Args:
            args: new attribute values
            kwargs: dictionary of attribute names and values
        """
        if args and args != ():
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except:
                pass
        else:
            for attr, val in kwargs.items():
                if attr == "id":
                    self.id = val
                else:
                    setattr(self, '_Rectangle__' + attr, val)

    def to_dictionary(self):
        """Public method returns dictionary representation"""
        return  {
            "id" : self.id,
            "width" : self.__width,
            "height" : self.__height,
            "x" : self.__x,
            "y" : self.__y
        }
