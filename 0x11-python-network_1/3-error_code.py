#!/usr/bin/python3
""" Module for Task 3 """

import sys
import urllib.request

try:
    with urllib.request.urlopen(sys.argv[1]) as resp:
        print(resp.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print("Error code: {}".format(e.code))
