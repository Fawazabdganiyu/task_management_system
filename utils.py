#!/usr/bin/python3
"""Utility functions for the project."""


def sorting_algorithm(task):
    """ Sorting algorithm for tasks in order of priority and due date
    Args:
        task (dict): Task dictionary
    Returns:
        tuple: Priority order and due date
    """
    priority_order = {
        ("Important", "Urgent"): 1,
        ("Important", "Not urgent"): 2,
        ("Not important", "Urgent"): 3,
        ("Not important", "Not urgent"): 4,
    }
    priority = task["priority"]
    return (priority_order[(priority["importance"], priority["urgency"])],
            task["due_date"])


def display_menu():
    """ Display menu options """
    print("Task Management System")
    print("1. Add a task")
    print("2. List tasks")
    print("3. Mark task as complete")
    print("4. Delete a task")
    print("5. Exit")


def get_task(task_id, tasks):
    """ Validate task index
    Args:
        task_id (str): Task id
        tasks (list): List of tasks
    Returns:
        dict: Task dictionary if task id is valid, None otherwise
    """
    if not tasks:
        print("\nNo tasks has been added!")
        return None

    if task_id not in tasks.keys():
        print("\nInvalid task id. Please try again.")
        return None

    return tasks[task_id]


def continue_execution():
    """ Check if user wants to continue execution
    Returns:
        bool: True if user wants to continue, False otherwise
    """
    next = input("\nDo you want to continue? (y/n): ")
    if next.lower() != "y":
        return False

    menu = input("\nDo you want to see the menu again? (y/n): ")
    if menu.lower() == "y":
        display_menu()

    return True


def generate_task_id(tasks):
    """ Get the task id
    Args:
        tasks (list): List of tasks
    Returns:
        str: Task id
    """
    # Get the last task id
    if not tasks:
        return "task_01"

    task_ids = [int(task_id.split("_")[1]) for task_id in tasks.keys()]
    task_ids.sort()

    return f"task_{task_ids[-1] + 1:02d}"
