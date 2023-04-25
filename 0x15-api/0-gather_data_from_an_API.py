#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
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

    user_name = user_response.json()["name"]
    todos = todos_response.json()
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task["completed"]]
    num_done_tasks = len(done_tasks)
    print("Employee {} is done with tasks({}/{}):"
          .format(user_name, num_done_tasks, total_tasks))

    for task in done_tasks:
        print("\t {} {}".format(task["title"], "(completed)"))


if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: {} employee_id".format(argv[0]))
        exit(1)
    try:
        get_employee_todos(argv[1])
    except ValueError as e:
        print(e)
        exit(1)#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
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

    user_name = user_response.json()["name"]
    todos = todos_response.json()
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task["completed"]]
    num_done_tasks = len(done_tasks)
    print("Employee {} is done with tasks({}/{}):"
          .format(user_name, num_done_tasks, total_tasks))

    for task in done_tasks:
        print("\t {} {}".format(task["title"], "(completed)"))


if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: {} employee_id".format(argv[0]))
        exit(1)
    try:
        get_employee_todos(argv[1])
    except ValueError as e:
        print(e)
        exit(1)
