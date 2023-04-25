#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress and exports data in CSV format.
"""

import requests
import csv
from sys import argv


def get_employee_todos(employee_id):
    """Returns information about the employee TODO list progress."""
    user_url = "https://jsonplaceholder.typicode.com/users/" + str(employee_id)
    todos_url = user_url + "/todos"
    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200:
        raise ValueError("User not found")
    if todos_response.status_code != 200:
        raise ValueError("Todos not found")

    user_name = user_response.json()["username"]
    todos = todos_response.json()
    rows = []
    for task in todos:
        row = [employee_id, user_name, task["completed"], task["title"]]
        rows.append(row)
    return rows


if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: {} employee_id".format(argv[0]))
        exit(1)
    try:
        employee_id = argv[1]
        rows = get_employee_todos(employee_id)
        file_name = employee_id + ".csv"
        with open(file_name, "w", newline="") as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC)
            writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            writer.writerows(rows)
        print("Data exported to", file_name)
    except ValueError as e:
        print(e)
        exit(1)
