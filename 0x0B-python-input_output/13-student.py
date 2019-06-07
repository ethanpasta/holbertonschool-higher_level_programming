#!/usr/bin/python3
"""Module 11-student"""


class Student:
    """Custom class Student"""

    def __init__(self, first_name, last_name, age):
        """Initialization function

        Args:
            first_name: first name of student
            last_name: last name of student
            age: age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns dictionary representation of a student instance"""
        my_dic = {}
        if list and all(isinstance(s, str) for s in attrs):
            for x in attrs:
                if x in self.__dict__:
                    my_dic[x] = self.__dict__[x]
            return my_dic
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the student instance"""
        for key in json:
            self.key = json[key]
