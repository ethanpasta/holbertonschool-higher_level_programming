#!/usr/bin/python3
""" Module for Task 1 """

import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as resp:
    print(dict(resp.info()).get('X-Request-Id'))
