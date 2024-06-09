"""Task management features"""
from datetime import datetime
from prettytable import PrettyTable

from file_storage import file_storage
from utils import sorting_algorithm, get_task, generate_task_id

tasks = file_storage.load_tasks()


def add_task(description, due_date, priority):
    """Add a new task"""
    try:
        due_date = datetime.strptime(due_date, "%d-%m-%Y %H:%M")
    except ValueError:
        print("\n\n----Aborting task creation----\n")
        print("Invalid date format. Please use DD-MM-YYYY H:M")
        return

    # Set default values for priority
    priority["importance"] = "Not important" if priority.get("importance") \
        not in ["Important", "Not important"] else priority["importance"]
    priority["urgency"] = "Not urgent" if priority.get("urgency") \
        not in ["Urgent", "Not urgent"] else priority["urgency"]

    # Add task to tasks list
    task_id = generate_task_id(tasks)
    task = {
        "task_id": task_id,
        "description": description,
        "due_date": due_date,
        "completed": False,
        "created_at": datetime.now(),
        "priority": priority,
        "Expired": "No"
    }
    tasks[task_id] = task

    # Save tasks to file
    file_storage.save_tasks(tasks)
    print("\nTask added successfully!")


def list_tasks():
    """List all tasks"""
    if not tasks:
        print("\nNo tasks has been added!")
        return

    # Sort tasks by priority then due date
    sorted_tasks = sorted(tasks.values(), key=sorting_algorithm)

    # Define the table and its headers
    table = PrettyTable()
    table.field_names = ["Task index", "Task id", "Created At",
                         "Description", "Due Date", "Status", "Expired"]

    for index, task in enumerate(sorted_tasks):
        status = "Completed" if task["completed"] else "Not Completed"
        # Add a row to the table for each task
        table.add_row([index + 1, task['task_id'], task['created_at'],
                       task['description'], task['due_date'],
                       status, task["Expired"]])

    # Print the table
    print(table)


def mark_task(task_id):
    """Mark a task as complete"""
    task = get_task(task_id, tasks)
    if not task:
        return

    # Check if task is already completed
    if task["completed"]:
        print("Task already marked as complete!")
        return

    # Mark task as complete
    tasks[task_id]["completed"] = True

    # Update tasks in file
    file_storage.save_tasks(tasks)

    print(f"Task {task_id} marked as complete!")


def delete_task(task_id):
    """Delete a task"""
    task = get_task(task_id, tasks)
    if not task:
        return

    # Delete task from tasks list
    del tasks[task_id]

    # Update tasks in file
    file_storage.save_tasks(tasks)
    print(f"Task {task_id} deleted successfully!")
