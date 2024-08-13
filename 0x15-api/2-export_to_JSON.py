#!/usr/bin/python3

"""Python script that, using this REST API returns information."""
import json
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    try:
        employee_id = int(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    base_url = "https://jsonplaceholder.typicode.com"
    user_url = "{}/users/{}".format(base_url, employee_id)
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Error: Unable to retrieve user information for employee\
            ID {}.".format(employee_id))
        sys.exit(1)

    user_data = user_response.json()
    employee_name = user_data['username']
    todos_url = "{}/todos?userId={}".format(base_url, employee_id)
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print("Error: Unable to retrieve TODO list for employee\
            ID {}.".format(employee_id))
        sys.exit(1)

    todos = todos_response.json()
    total_tasks = len(todos)
    completed_tasks = [task for task in todos if task['completed']]
    number_of_completed_tasks = len(completed_tasks)

    tasks =[]
    for task in todos:
        task_dict = {
            "tasks": task['title'],
            "completed": task['completed'],
            "username": employee_name
        }
        tasks.append(task_dict)
    data = {str(employee_id): task}

    file_name = "{}.json".format(employee_id)
    with open(file_name, 'w') as outfile:
        json.dump(data, outfile)
    print("Data exported to {}".format(file_name))
