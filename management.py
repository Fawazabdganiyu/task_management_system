#!/usr/bin/env python3
""" Task Management Module """
from datetime import datetime

from features import add_task, list_tasks, mark_task, delete_task
from utils import display_menu, continue_execution


def main():
    """ Main function """
    display_menu()
    while True:
        try:
            choice = input("\nPlease make your choice: ")
        except ValueError:
            print("Invalid option. Please try again.")
            continue
        print()
        if choice == "1":
            description = input("Enter task description: ")
            due_date = input("Enter due date and time in the format DD-MM-YYYY H:M ")
            priority = {
                "importance": input("Enter importance (Important/Not important): "),
                "urgency": input("Enter urgency (Urgent/Not urgent): ")
            }
            add_task(description, due_date, priority)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            task_id = input("Enter task id that is completed: ")
            mark_task(task_id)
        elif choice == "4":
            task_id = input("Enter task id to delete: ")
            delete_task(task_id)
        elif choice == "5":
            print("Exiting the Task Management System. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

        if not continue_execution():
            break


if __name__ == "__main__":
    main()
