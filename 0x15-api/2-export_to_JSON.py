#!/usr/bin/python3
"""
extend python script to export
data in the JSON format
"""
import json
import requests
import sys


if __name__ == '__main__':
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    r1 = requests.get(url + "users/{}".format(id))
    params = {'userId': id}
    r2 = requests.get(url + "todos", params=params)
    uname = r1.json().get("username")
    todo_list = r2.json()
    full_list = []
    for task in todo_list:
        full_list.append({"task": task.get("title"),
                          "completed": task.get("completed"),
                          "username": uname})
    user_dict = {id: full_list}
    with open("{}.json".format(id), "w") as f:
        json.dump(user_dict, f)
