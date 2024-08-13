#!/usr/bin/python3

"""Python script that, using this REST API returns information."""
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
    employee_name = user_data['name']
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

    print("Employee {} is done with tasks({}/{}):".format(employee_name,\
                                                          number_of_completed_tasks, total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task['title']))
