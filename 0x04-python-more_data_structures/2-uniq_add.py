#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = []
    for x in my_list:
        if x not in uniq_list:
            uniq_list.append(x)
    return sum(uniq_list)
