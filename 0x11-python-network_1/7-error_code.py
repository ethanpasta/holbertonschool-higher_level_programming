#!/usr/bin/python3
""" Module for task 7 """

import requests
import sys


resp = requests.get(sys.argv[1])
if resp.status_code >= 400:
    print("Error code: {}".format(resp.status_code))
else:
    print(resp.text)
