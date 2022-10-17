#!/usr/bin/python3

import json
import os
import requests
import sys


if __name__ == '__main__':
    employer_id = sys.argv[1]
    res1 = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employer_id))

    res2 = requests.get(
        "https://jsonplaceholder.typicode.com/todos")

    total_number_of_task = 0
    number_of_done_task = 0
    employer_name = res1.json()['name']
    titles = []

    for data in res2.json():
        if data.get('userId') == int(employer_id):
            total_number_of_task += 1

            if data['completed'] is True:
                number_of_done_task += 1
                titles.append(data['title'])
        else:
            continue

    print("Employee {} is done with tasks({}/{}):".format(employer_name,
          number_of_done_task, total_number_of_task))
    for title in titles:
        print("\t {}".format(title))
