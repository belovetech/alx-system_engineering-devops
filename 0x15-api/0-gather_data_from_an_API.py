#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys


if __name__ == '__main__':
    # url = "https://jsonplaceholder.typicode.com"
    employer_id = sys.argv[1]

    res1 = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employer_id))

    res2 = requests.get(
        "https://jsonplaceholder.typicode.com/todos")

    total_number_of_task = 0
    number_of_done_task = 0
    employer_name = res1.json().get('name')
    titles = []

    for data in res2.json():
        if data.get('userId') == int(employer_id):
            total_number_of_task += 1

            if data.get('completed') is True:
                number_of_done_task += 1
                titles.append(data.get('title'))
        else:
            continue

    print("Employee {} is done with tasks({}/{}):".format(employer_name,
          number_of_done_task, total_number_of_task))
    for title in titles:
        print("\t {}".format(title))
