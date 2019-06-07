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

    def to_json(self, attrs=None):
        """Returns dictionary representation of a student instance

        Args:
            attrs: list of attributes
        """
        if type(attrs) is not list or not all(
                isinstance(s, str) for s in attrs):
            return self.__dict__
        my_dic = {}
        for x in attrs:
            try:
                my_dic[x] = self.__dict__[x]
            except:
                pass
            return my_dic

    def reload_from_json(self, json):
        """Replace all attributes of the student instance"""
        for k, v in json:
            try:
                self.__dict__[k] = v
            except:
                pass
