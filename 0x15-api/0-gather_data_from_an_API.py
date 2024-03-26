#!/usr/bin/python3
"""
A pyhton script that, using this REST API for a
employee's id, returns information about his/her
TODO list
"""

import requests
import sys


if __name__ == '__main__':
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    r1 = requests.get(url + "users/{}".format(id))
    r2 = requests.get(url + "todos?userId={}".format(id))
    name = r1.json().get('name')
    todo_list = r2.json()
    completed = [x.get('title') for x in todo_list
                 if x.get('completed') is True]
    print("Employee {} is done with tasks({}/{}):".format(
        name, len(completed), len(todo_list)))
    for y in completed:
        print("\t {}".format(y))
