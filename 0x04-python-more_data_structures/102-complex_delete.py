#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    delete = [key for key in a_dictionary.keys() if a_dictionary[key] == value]
    if delete:
        for key in delete:
            del a_dictionary[key]
    return a_dictionary
