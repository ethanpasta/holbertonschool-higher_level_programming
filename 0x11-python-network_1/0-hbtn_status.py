#!/usr/bin/python3
""" Module for Task 0 """

import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as resp:
    response = resp.read()
    print("Body response:")
    print("    - type: {}".format(type(response)))
    print("    - content: {}".format(response))
    print("    - utf8 content: {}".format(response.decode('utf-8')))
