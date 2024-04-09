#!/usr/bin/python3
"""
Recursive function that queries the reddit api and
returns a list containing the titles of all hot articles
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    Returns a list containing
    the titles of all hot articles
    Params:
        subreddit (str): subreddit name
        hot_list (list): list of hot articles
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "reddit/0.0.1"}
    params = {"after": after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    else:
        results = response.json()
        if len(results['data']['children']) == 0:
            return hot_list
        else:
            for post in results['data']['children']:
                hot_list.append(post['data']['title'])
            after = results['data']['after']
            if after:
                return recurse(subreddit, hot_list, after)
            return hot_list
