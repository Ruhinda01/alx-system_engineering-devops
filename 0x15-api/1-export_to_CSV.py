#!/usr/bin/python3
"""
Extend your python script to export data
in the CSV format
"""

if __name__ == '__main__':
    import csv
    import requests
    import sys

    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    r1 = requests.get(url + "users/{}".format(id))
    r2 = requests.get(url + "users/{}/todos".format(id))
    uname = r1.json().get('username')
    todo_list = r2.json()
    with open("{}.csv".format(id), "w") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todo_list:
            writer.writerow([id, uname,
                             task.get('completed'), task.get('title')])
