#!/usr/bin/python3
def no_c(my_string):
    i = 0
    my_list = list(my_string)
    for ch in my_list:
        if ch == 'c' or ch == 'C':
            del my_list[i]
        i = i + 1
    return ''.join(my_list)
