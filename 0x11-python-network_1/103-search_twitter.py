#!/usr/bin/python3
""" Module for task 13 """

if __name__ == "__main__":
    import requests
    import sys
    import base64

    auth = "{}:{}".format(sys.argv[1], sys.argv[2]).encode('ascii')
    auth_64 = base64.b64encode(auth).decode('ascii')
    headers = {
        'Authorization': 'Basic ' + auth_64,
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }
    data = {'grant_type': 'client_credentials'}
    r = requests.post("https://api.twitter.com/oauth2/token",
                      data=data, headers=headers)
    d = r.json()
    if d.get('token_type') != "bearer":
        print("Not found")
        exit()
    access_token = d.get('access_token')

    new_header = {"Authorization": "Bearer " + access_token}
    new_body = {"q": sys.argv[3], "count": 5}
    r = requests.get("https://api.twitter.com/1.1/search/tweets.json",
                     params=new_body, headers=new_header)
    tweets = r.json().get('statuses')
    for tweet in tweets:
        print("[{}] {} by {}".format(
            tweet.get('id'),
            tweet.get('text'),
            tweet.get('user').get('name')))
