#!/usr/bin/python3
""" Module for Task 0 """

if __name__ == "__main__":

    import urllib.request

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as resp:
        response = resp.read()
        print("Body response:")
        print('\t- type: {}'.format(type(response)))
        print('\t- content: {}'.format(response))
        print('\t- utf8 content: {}'.format(response.decode('utf-8')))
