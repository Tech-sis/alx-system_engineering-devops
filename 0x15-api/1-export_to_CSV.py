#!/usr/bin/python3
"""
Request from API; Return TODO list progress given employee ID
Export this data to CSV
"""
import csv
import requests
from sys import argv


def to_csv():
    """return API data"""
    users = requests.get('https://jsonplaceholder.typicode.com/users/')
    for i in users.json():
        if i.get('id') == int(argv[1]):
            USERNAME = (i.get('username'))
            break
    TASK_STATUS_TITLE = []
    todos = requests.get("https://jsonplaceholder.typicode.com/todos/")
    for t in todos.json():
        if t.get('userId') == int(argv[1]):
            TASK_STATUS_TITLE.append([t.get('completed'), t.get('title')])
    """export to CSV"""
    filename = "{}.csv".format(argv[1])
    with open(filename, 'w') as csvfile:
        fieldnames = ["USER_ID", "USERNAME",
                      "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(
            csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        for task in TASK_STATUS_TITLE:
            writer.writerow({"USER_ID": argv[1], "USERNAME": USERNAME,
                            "TASK_COMPLETED_STATUS": task[0],
                             "TASK_TITLE": task[1]})


if __name__ == "__main__":
    to_csv()
