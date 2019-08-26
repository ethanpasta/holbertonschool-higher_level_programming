#!/usr/bin/python3
""" Module for Task 6 """

if __name__ == "__main__":

    import requests
    import sys

    resp = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(resp.text)
