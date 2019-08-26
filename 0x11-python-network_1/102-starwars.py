#!/usr/bin/python3
""" Module for task 13 """


def parse(data):
    for person in data['results']:
        print(person.get('name'))
        films = person.get('films')
        for film in films:
            print('\t{}'.format(requests.get(film).json().get('title')))
    if data.get('next') is not None:
        parse(requests.get(data.get('next')).json())


if __name__ == "__main__":
    import requests
    import sys

    url = "https://swapi.co/api/people/?search={}".format(sys.argv[1])
    r = requests.get(url)
    data = r.json()
    print("Number of results: {}".format(data.get('count')))
    parse(data)
