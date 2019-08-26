#!/usr/bin/python3
""" Module for task 100 """

if __name__ == "__main__":

    import requests
    import sys

    r = requests.get("https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1]))
    data = r.json()
    for t in data[0:10]:
        print("{}: {}".format(t.get('sha'), t.get('author').get('name')))
