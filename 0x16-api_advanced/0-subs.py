#!/usr/bin/python3
"""Fetch number of subscribers from subreddit API"""
import requests


def number_of_subscribers(subreddit):
    """Return number of subscribers
    Args:
        subreddit (str): subreddit
    Returns:
        (int): Number of the subscribers
    """
    headers = {'User-agent': 'myAPI'}
    listing = 'top'
    limit = 100
    timeframe = 'month'

    try:
        base_url = 'https://www.reddit.com/r/{}/{}.json?limit={}&t={}'.format(
                                subreddit, listing, limit, timeframe)
        res = requests.get(base_url, headers=headers)
        for post in res.json()['data']['children']:
            for key, value in post['data'].items():
                if key == 'subreddit_subscribers':
                    return value
    except Exception:
        return 0
