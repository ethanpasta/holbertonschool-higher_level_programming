#!/usr/bin/python3
""" Module for task 8 """


def parse(url, pr):
        r = requests.get(url)
        data = r.json()
        if data:
            if pr == 0:
                print("Number of results: {}".format(data.get('count')))
            for dic in data.get('results'):
                print(dic.get('name'))
            if data.get('next'):
                parse(data.get('next'), 1)

if __name__ == "__main__":

    import requests
    import sys

    url = "https://swapi.co/api/people/?search={}".format(sys.argv[1])
    parse(url, 0)
