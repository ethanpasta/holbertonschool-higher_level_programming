#!/usr/bin/python3
""" Module for Task 4 """

import requests

resp = requests.get('https://intranet.hbtn.io/status')
print("Body response:")
print("    - type: {}".format(type(resp.text)))
print("    - content: {}".format(resp.text))
