#!/usr/bin/python3
""" Module for task 8 """

if __name__ == "__main__":

    import requests
    import sys

    url = "https://swapi.co/api/people/?search={}".format(sys.argv[1])
    r = requests.get(url)
    data = r.json()
    if data:
        print("Number of results: {}".format(data['count']))
        for dic in data['results']:
            print(dic['name'])
