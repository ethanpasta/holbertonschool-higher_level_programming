#!/usr/bin/python3
def remove_char_at(str, n):
    s = ''
    i = 0
    if n < 0 or n > len(str):
        return str
    for c in str:
        if i != n:
            s += c
        i += 1
    return s
