#!/usr/bin/python3
"""Recursive function that queries the Reddit API"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Get titles of top 10 hot posts
    Args:
        subreddit (str): subreddit
        hot_list (list): hot list
    Returns:
        (str): titles of top 10 posts
    """
    headers = {'User-agent': 'myAPI'}
    params = {
        'after': after,
        'count': count,
        'limit': 100
    }
    base_url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    res = requests.get(base_url, headers=headers,
                       params=params, allow_redirects=False)
    if res.status_code == 404:
        return None

    results = res.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for post in results.get("children"):
        hot_list.append(post.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
