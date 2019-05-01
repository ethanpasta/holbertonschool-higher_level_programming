#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) <= ord('z') and ord(c) >= ord('a'):
            print("{:c}".format(ord(c) - 32), end='')
        else:
            print(c, end='')
    print("")
