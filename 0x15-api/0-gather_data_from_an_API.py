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
    params = {'userId': id}
    r2 = requests.get(url + "todos", params=params)
    name = r1.json().get("name")
    todo_list = r2.json()
    completed = [t.get("title") for t in todo_list
                 if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        name, len(completed), len(todo_list)))
    for task in completed:
        print("\t {}".format(task))
