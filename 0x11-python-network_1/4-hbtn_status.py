#!/usr/bin/python3
""" Module for Task 4 """

if __name__ == "__main__":

    import requests

    resp = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print('\t- type: {}'.format(type(resp.text)))
    print('\t- content: {}'.format(resp.text))
