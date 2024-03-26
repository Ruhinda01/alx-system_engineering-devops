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
    r2 = requests.get(url + "users/{}/todos".format(id))
    name = r1.json().get("name")
    todo_list = r2.json()
    tasks = len(todo_list)
    completed = 0
    for task in todo_list:
        if task.get('completed') is True:
            completed += 1
    print("Employee {} is done with tasks({}/{}):".format(
        name, completed, tasks))
    for done in todo_list:
        if done.get('completed') is True:
            print("\t {}".format(done.get('title')))
