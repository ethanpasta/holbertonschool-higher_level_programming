#!/usr/bin/python3
""" Module for task 100 """

def parse(url, num):
    r = requests.get(url)
    data = r.json()
    for t in data:
        print("{}: {}".format(t.get('commit').get('tree').get('sha'),
                              t.get('commit').get('committer').get('name')))
    if 'next' in r.links.keys() and num == 0:
        parse(r.links.get('next').get('url'), 1)

if __name__ == "__main__":

    import requests
    import sys

    parse("https://api.github.com/repos/{}/{}/commits?per_page=5&page=1"
          .format(sys.argv[2], sys.argv[1]), 0)
