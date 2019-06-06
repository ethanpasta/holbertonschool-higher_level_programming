#!/usr/bin/python3
class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def to_json(self, attrs=None):
        my_dic = {}
        if isinstance(attrs, list) and all(isinstance(s, str) for s in attrs):
            for x in attrs:
                if x in self.__dict__:
                    my_dic[x] = self.__dict__[x]
            return my_dic
        return self.__dict__
    def reload_from_json(self, json):
        for key in json:
            self.key = json[key]
