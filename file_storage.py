#!/usr/bin/python3
""" File Storage Module """
from datetime import datetime
import json


class FileStorage:
    """ File Storage Class """

    __filename = "tasks.json"
    __date_format = "%d-%m-%Y %H:%M"

    # Save tasks to json file
    @staticmethod
    def save_tasks(tasks):
        """ Save tasks to file """
        tasks_copy = tasks.copy()
        # Format datetime objects for json serialization
        for task in tasks_copy.values():
            if isinstance(task["due_date"], datetime):
                task["due_date"] = task["due_date"]\
                    .strftime(FileStorage.__date_format)
            if isinstance(task["created_at"], datetime):
                task["created_at"] = task["created_at"]\
                    .strftime(FileStorage.__date_format)

            # Update task deadline status
            if task["due_date"] < datetime.now()\
               .strftime(FileStorage.__date_format):
                task["Expired"] = "Yes"
        with open(FileStorage.__filename, "w") as file:
            json.dump(tasks_copy, file)

    # Load tasks from json file
    @staticmethod
    def load_tasks():
        """ Load tasks from file """
        try:
            with open(FileStorage.__filename, "r") as file:
                tasks = json.load(file)
            # Parse datetime strings to datetime objects
            for task in tasks.values():
                task["due_date"] = datetime.strptime(task["due_date"],
                                                     FileStorage.__date_format)
                task["created_at"] = datetime.strptime(
                    task["created_at"],
                    FileStorage.__date_forma
                )
        except FileNotFoundError:
            tasks = {}

        return tasks


# Initialize file storage
file_storage = FileStorage()
