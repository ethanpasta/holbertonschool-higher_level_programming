#!/usr/bin/python3
import sys
sum = 0
for arg in sys.argv[1:]:
    sum += int(arg)
print("{:d}".format(sum))
