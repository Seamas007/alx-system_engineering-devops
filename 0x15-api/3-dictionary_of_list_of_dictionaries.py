#!/usr/bin/python3
"""
Exports tasks for all employees to a JSON file
"""
import json
import requests


if __name__ == '__main__':
    # Set variables
    api_url = 'https://jsonplaceholder.typicode.com'
    employees_url = '{}/users'.format(api_url)
    todos_url = '{}/todos'.format(api_url)

    # Get employees
    employees_response = requests.get(employees_url)
    employees_list = employees_response.json()

    # Get todos for all employees
    todos_response = requests.get(todos_url)
    todos_list = todos_response.json()

    # Create dictionary of tasks
    tasks_dict = {}
    for employee in employees_list:
        employee_id = employee['id']
        employee_username = employee['username']
        employee_tasks = []
        for todo in todos_list:
            if todo['userId'] == employee_id:
                task_title = todo['title']
                task_completed = todo['completed']
                task_dict = {
                    'username': employee_username,
                    'task': task_title,
                    'completed': task_completed
                }
                employee_tasks.append(task_dict)
        tasks_dict[employee_id] = employee_tasks

    # Write tasks to JSON file
    json_filename = 'todo_all_employees.json'
    with open(json_filename, mode='w', encoding='utf-8') as json_file:
        json.dump(tasks_dict, json_file)#!/usr/bin/python3
"""
Exports tasks for all employees to a JSON file
"""
import json
import requests


if __name__ == '__main__':
    # Set variables
    api_url = 'https://jsonplaceholder.typicode.com'
    employees_url = '{}/users'.format(api_url)
    todos_url = '{}/todos'.format(api_url)

    # Get employees
    employees_response = requests.get(employees_url)
    employees_list = employees_response.json()

    # Get todos for all employees
    todos_response = requests.get(todos_url)
    todos_list = todos_response.json()

    # Create dictionary of tasks
    tasks_dict = {}
    for employee in employees_list:
        employee_id = employee['id']
        employee_username = employee['username']
        employee_tasks = []
        for todo in todos_list:
            if todo['userId'] == employee_id:
                task_title = todo['title']
                task_completed = todo['completed']
                task_dict = {
                    'username': employee_username,
                    'task': task_title,
                    'completed': task_completed
                }
                employee_tasks.append(task_dict)
        tasks_dict[employee_id] = employee_tasks

    # Write tasks to JSON file
    json_filename = 'todo_all_employees.json'
    with open(json_filename, mode='w', encoding='utf-8') as json_file:
        json.dump(tasks_dict, json_file)
