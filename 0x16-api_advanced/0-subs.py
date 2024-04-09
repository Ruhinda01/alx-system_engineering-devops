#!/usr/bin/python3
"""Function that queries the reddit api
and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the reddit api and returns
    the number of subscribers
    Params:
        subreddit (str): subreddit name
    Return:
        0 if subreddit does not exist
        number of subscribers
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Ruhinda"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0
    subs = response.json()
    return subs["data"]["subscribers"]
