#!/usr/bin/python3
"""Module for squaure class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Custom class for square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialization method

        Args:
            size: size
            x: x
            y: y
            id: id
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of sqaure object"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter for size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size attribute

        Args:
            value: new value
        """
        self.width = value
        self.height = value

    def __update_help(self, id=None, size=None, x=None, y=None):
        """Private internal method to update class attributes"""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """ Update class attributes

        Args:
            args: new attribute values
            kwargs: attribute names and new values
        """
        if args:
            self.__update_help(*args)
        elif kwargs:
            self.__update_help(**kwargs)

    def to_dictionary(self):
        """Public method returns dictionary representation"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
