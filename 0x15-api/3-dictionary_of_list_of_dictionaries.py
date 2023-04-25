#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            b.get("id"): [{
                "task": e.get("title"),
                "completed": e.get("completed"),
                "username": b.get("username")
            } for e in requests.get(url + "todos",
                                    params={"userId": b.get("id")}).json()]
            for b in users}, jsonfile)
