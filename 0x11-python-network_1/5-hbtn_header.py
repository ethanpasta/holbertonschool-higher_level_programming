#!/usr/bin/python3
""" Module for Task 5 """

if __name__ == "__main__":

    import requests
    import sys

    resp = requests.get(sys.argv[1])
    print(resp.headers.get('X-Request-Id'))
