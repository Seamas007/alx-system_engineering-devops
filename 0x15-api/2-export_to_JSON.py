#!/usr/bin/python3
"""
Exports tasks owned by an employee to a JSON file
"""
import json
import requests
import sys


if __name__ == '__main__':
    # Check command-line arguments
    if len(sys.argv) != 2:
        print('Usage: {} EMPLOYEE_ID'.format(sys.argv[0]))
        sys.exit(1)

    # Set variables
    api_url = 'https://jsonplaceholder.typicode.com'
    employee_id = sys.argv[1]
    employee_url = '{}/users/{}'.format(api_url, employee_id)
    todos_url = '{}/todos?userId={}'.format(api_url, employee_id)

    # Get employee info
    employee_response = requests.get(employee_url)
    employee_dict = employee_response.json()
    employee_username = employee_dict['username']

    # Get todos for employee
    todos_response = requests.get(todos_url)
    todos_list = todos_response.json()

    # Create dictionary of tasks
    tasks_dict = {}
    for todo in todos_list:
        task_title = todo['title']
        task_completed = todo['completed']
        task_dict = {
            'task': task_title,
            'completed': task_completed,
            'username': employee_username
        }
        if task_completed:
            status = 'completed'
        else:
            status = 'not completed'
        tasks_dict.setdefault(status, []).append(task_dict)

    # Write tasks to JSON file
    json_filename = '{}.json'.format(employee_id)
    with open(json_filename, mode='w', encoding='utf-8') as json_file:
        json.dump(tasks_dict, json_file)#!/usr/bin/python3
"""
Exports tasks owned by an employee to a JSON file
"""
import json
import requests
import sys


if __name__ == '__main__':
    # Check command-line arguments
    if len(sys.argv) != 2:
        print('Usage: {} EMPLOYEE_ID'.format(sys.argv[0]))
        sys.exit(1)

    # Set variables
    api_url = 'https://jsonplaceholder.typicode.com'
    employee_id = sys.argv[1]
    employee_url = '{}/users/{}'.format(api_url, employee_id)
    todos_url = '{}/todos?userId={}'.format(api_url, employee_id)

    # Get employee info
    employee_response = requests.get(employee_url)
    employee_dict = employee_response.json()
    employee_username = employee_dict['username']

    # Get todos for employee
    todos_response = requests.get(todos_url)
    todos_list = todos_response.json()

    # Create dictionary of tasks
    tasks_dict = {}
    for todo in todos_list:
        task_title = todo['title']
        task_completed = todo['completed']
        task_dict = {
            'task': task_title,
            'completed': task_completed,
            'username': employee_username
        }
        if task_completed:
            status = 'completed'
        else:
            status = 'not completed'
        tasks_dict.setdefault(status, []).append(task_dict)

    # Write tasks to JSON file
    json_filename = '{}.json'.format(employee_id)
    with open(json_filename, mode='w', encoding='utf-8') as json_file:
        json.dump(tasks_dict, json_file)
