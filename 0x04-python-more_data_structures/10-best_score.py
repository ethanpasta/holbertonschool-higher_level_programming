#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max = sorted(a_dictionary.values())[0]
    for key in a_dictionary.keys():
        if a_dictionary[key] == max:
            return key
