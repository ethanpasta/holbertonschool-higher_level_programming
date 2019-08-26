#!/usr/bin/python3
""" Module for Task 5 """

import requests
import sys

resp = requests.get(sys.argv[1])
print(resp.headers['X-Request-Id'])
