#!/usr/bin/python3
""" Module for task 10 """

if __name__ == "__main__":

    import requests
    import sys

    data = {'password': sys.argv[2]}
    login = requests.get('https://api.github.com/users/' + sys.argv[1], data=data)
    if login:
        print(login.json()['id'])
    else:
        print("None")
