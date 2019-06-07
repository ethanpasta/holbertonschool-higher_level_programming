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
        return self.__dict__
