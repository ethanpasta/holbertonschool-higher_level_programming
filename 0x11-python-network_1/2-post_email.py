#!/usr/bin/python3
""" Module for Task 2 """

import urllib.request
import urllib.parse

import sys

data = urllib.parse.urlencode({'email': sys.argv[2]}).encode('utf-8')
with urllib.request.urlopen(url=sys.argv[1], data=data) as resp:
    print(resp.read().decode('utf-8'))
