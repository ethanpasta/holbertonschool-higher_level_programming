#!/usr/bin/python3
""" Module for task 10 """

if __name__ == "__main__":

    import requests
    import sys

    login = requests.get(
        'https://api.github.com/user', auth=(sys.argv[1], sys.argv[2]))
    if login.status_code < 400:
        print(login.json().get('id'))
    else:
        print("None")
