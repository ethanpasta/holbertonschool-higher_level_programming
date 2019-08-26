#!/usr/bin/python3
""" Module for task 8 """

if __name__ == "__main__":

    import requests
    import sys

    let = ""
    if len(sys.argv) >= 2:
        let = sys.argv[1]
    resp = requests.post('http://0.0.0.0:5000/search_user', data={'q': let})
    try:
        j = resp.json()
        if j == {}:
            print("No result")
        else:
            print("[{}] {}".format(j['id'], j['name']))
    except ValueError:
        print("Not a valid JSON")
