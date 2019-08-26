#!/usr/bin/python3
""" Module for Task 6 """

import requests
import sys

resp = requests.post(sys.argv[1], data={'email': sys.argv[2]})
print(resp.text)
