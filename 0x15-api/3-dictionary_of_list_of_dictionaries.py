#!/usr/bin/python3
"""Python script that gathers data from a REST API for all employees."""
import json
import requests
import sys

if __name__ == '__main__':
    base_url = "https://jsonplaceholder.typicode.com"


    users_url = "{}/users".format(base_url)
    users_response = requests.get(users_url)
    if users_response.status_code != 200:
        print("Error: Unable to retrieve user information.")
        sys.exit(1)

    users_data = users_response.json()

    todos_url = "{}/todos".format(base_url)
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print("Error: Unable to retrieve TODO list.")
        sys.exit(1)
    
    todos = todos_response.json()

    data = {}

    for user in users_data:
        user_id = str(user['id'])
        user_name = user['username']
        user_tasks = [
            {
                "username": user_name,
                "task": todo['title'],
                "completed": todo["completed"],
            }
            for todo in todos if todo['userId'] == int(user_id)
        ]
        data[user_id] = user_tasks

    with open("todo_all_employees.json", "w") as f:
        json.dump(data, f)
