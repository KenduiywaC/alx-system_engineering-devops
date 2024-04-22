#!/usr/bin/python3

"""
Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.
"""
import requests
import sys

def get_employee_todo_progress(employee_id):
    if __name__ == "__main__":
        url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
        response = requests.get(url)
        if response.status_code != 200:
            print("Error: Failed to fetch data from the API.")

            todos = response.json()
            employee_name = todos[0]['username']
            total_tasks = len(todos)
            done_tasks = sum(1 for todo in todos if todo['completed'])

            print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
            for todo in todos:
                if todo['completed']:
                    print(f"\t{todo['title']}")

                    if __name__ == "__main__":
                        if len(sys.argv) != 2:
                            print("Usage: python3 gather_data_from_an_API.py <employee_id>")
                        else:
                            employee_id = sys.argv[1]
                            get_employee_todo_progress(employee_id)
