#!/usr/bin/python3
"""
Records all tasks from all employees
"""
import json
import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    file = "todo_all_employees.json"
    r1 = requests.get(url + "users/")
    users = r1.json()
    user_dict = {}
    full_list = []
    for user in users:
        r2 = requests.get(url + "todos", params={user.get("id"): id})
        todo_list = r2.json()
        uname = user.get("username")
        for task in todo_list:
            full_list.append({"task": task.get("title"),
                              "completed": task.get("completed"),
                              "username": uname})
        user_dict[user.get("id")] = full_list
    with open(file, "w") as f:
        json.dump(user_dict, f)
