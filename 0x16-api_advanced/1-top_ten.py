#!/usr/bin/python3
"""Fetch titles of top 10 hot posts subreddit API"""
import requests


def top_ten(subreddit):
    """Get titles of top 10 hot posts
    Args:
        subreddit (str): subreddit
    Returns:
        (str): titles of top 10 posts
    """
    headers = {'User-agent': 'myAPI'}
    params = {
        'limit': 10
    }
  

    try:
        base_url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
        res = requests.get(base_url, headers=headers, params=params, allow_redirects=False)
        for post in res.json()['data']['children']:
            for key, value in post['data'].items():
                if key == 'title':
                    print(value)
    except Exception:
        print(None)
