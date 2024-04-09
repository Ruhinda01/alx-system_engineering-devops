#!/usr/bin/python3
"""
Function that queries the reddit api and
prints the titles of the first 10 hot posts
"""
import requests


def top_ten(subreddit):
    """
    Queries the reddit api and
    prints the titles of the first 10 hot posts
    Params:
        subreddit (str): subreddit name
    Return:
        None
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Ruhinda"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print('None')
    posts = response.json()
    if len(posts['data']['children']) == 0:
        print('None')
    for index, post in enumerate(posts['data']['children']):
        if index < 10:
            print(post['data']['title'])
