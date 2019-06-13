#!/usr/bin/python3
"""Module base class"""


import json
import csv


class Base:
    """Custom base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization method

        Args:
            id: id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method returns JSON string representation"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Class method writes JSON string representation to file"""
        new_list = [] if list_objs is None else [
            x.to_dictionary() for x in list_objs]
        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w+') as f:
            f.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """Static method returns list of the JSON string representation

        Args:
            json_string: json string
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Class method returns instance with all attributes already set

        Args:
            cls: class
            dictionary: dictionary of attribute names and values
        """
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            dummy = Rectangle(1, 1)
        elif cls is Square:
            dummy = Square(1)
        else:
            dummy = None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Class method returns list of instances

        Args:
            cls: class
        """
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename) as f:
                return [cls.create(
                    **d) for d in cls.from_json_string(f.read())]
        except:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        from models.rectangle import Rectangle
        from models.square import Square
        filename = "{}.csv".format(cls.__name__)
        write_l = []
        if cls is Rectangle:
            for obj in list_objs:
                write_l.append([obj.id, obj.width, obj.height, obj.x, obj.y])
        elif cls is Square:
            for obj in list_objs:
                write_l.append(obj.id, obj.size, obj.x, obj.y)
        with open(filename, 'w+', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(write_l)
