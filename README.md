# Task Management System
## Overview
The `Task Management System` is a command-line application designed to help users manage their tasks efficiently. Users can add, list, mark tasks as complete, and delete tasks. Each task has a description, due date and time, importance, urgency, and completion and expiration status.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Author](#author)

## Features
- **`Add a Task`**: Users can add tasks with a `description`, `due date and time`, `importance`, and `urgency`.
- **`List Tasks`**: View all tasks with details like description, `due date`, `priority`, and `completion status`.
- **`Mark Task as Complete`**: Update the status of a task to completed.
- **`Delete a Task`**: Remove a task from the list.
- **`Persistent Storage`**: Tasks are saved to a file and loaded automatically when the application starts.

## Installation
1. Clone the repository:
```bash
git clone https://github.com/fawazabdganiyu/task_management_system.git
cd task_management_system
```

2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. Install the dependencies:
```bash
pip install -r requirements.txt
```

4. Make the `management.py` module executable
```bash
chmod u+x management.py
```

## Usage
Run the application using the following command:
```bash
./management.py
```

## Examples
Here is an example interaction with the application:
```bash
Task Management System
1. Add a task
2. List tasks
3. Mark task as complete
4. Delete a task
5. Exit

Please make your choice: 1

Enter task description: Revision
Enter due date and time in the format DD-MM-YYYY H:M 10-6-2024 22:00
Enter importance (Important/Not important): Important
Enter urgency (Urgent/Not urgent):

Task added successfully!

Do you want to continue? (y/n): y

Do you want to see the menu again? (y/n): 2

Please make your choice: 2

+------------+---------+------------------+-------------+------------------+---------------+---------+
| Task index | Task id |    Created At    | Description |     Due Date     |     Status    | Expired |
+------------+---------+------------------+-------------+------------------+---------------+---------+
|     1      | task_01 | 09-06-2024 20:08 |   Revision  | 10-06-2024 22:00 | Not Completed |    No   |
|     2      | task_02 | 09-06-2024 20:09 |   Revision  | 10-06-2024 22:00 | Not Completed |    No   |
+------------+---------+------------------+-------------+------------------+---------------+---------+

Do you want to continue? (y/n): y

Do you want to see the menu again? (y/n):

Please make your choice: 4

Enter task id to delete: task_02
Task task_02 deleted successfully!

Do you want to continue? (y/n): y

Do you want to see the menu again? (y/n):

Please make your choice: 2

+------------+---------+------------------+-------------+------------------+---------------+---------+
| Task index | Task id |    Created At    | Description |     Due Date     |     Status    | Expired |
+------------+---------+------------------+-------------+------------------+---------------+---------+
|     1      | task_01 | 09-06-2024 20:08 |   Revision  | 10-06-2024 22:00 | Not Completed |    No   |
+------------+---------+------------------+-------------+------------------+---------------+---------+

Do you want to continue? (y/n): y

Do you want to see the menu again? (y/n): n

Please make your choice: 1

Enter task description: Refactor Kajola App
Enter due date and time in the format DD-MM-YYYY H:M 11-6-2024 9:00
Enter importance (Important/Not important): Important
Enter urgency (Urgent/Not urgent): Not urgent

Task added successfully!

Do you want to continue? (y/n): y

Do you want to see the menu again? (y/n):

Please make your choice: 2

+------------+---------+------------------+---------------------+------------------+---------------+---------+
| Task index | Task id |    Created At    |     Description     |     Due Date     |     Status    | Expired |
+------------+---------+------------------+---------------------+------------------+---------------+---------+
|     1      | task_01 | 09-06-2024 20:08 |       Revision      | 10-06-2024 22:00 | Not Completed |    No   |
|     2      | task_02 | 09-06-2024 20:14 | Refactor Kajola App | 11-06-2024 09:00 | Not Completed |    No   |
+------------+---------+------------------+---------------------+------------------+---------------+---------+

Do you want to continue? (y/n): y

Do you want to see the menu again? (y/n):

Please make your choice: 1

Enter task description: Make laundry for next outing
Enter due date and time in the format DD-MM-YYYY H:M 10-06-2024 8:00
Enter importance (Important/Not important): Important
Enter urgency (Urgent/Not urgent): Not urgent

Task added successfully!

Do you want to continue? (y/n): y

Do you want to see the menu again? (y/n): n

Please make your choice: 2

+------------+---------+------------------+------------------------------+------------------+---------------+---------+
| Task index | Task id |    Created At    |         Description          |     Due Date     |     Status    | Expired |
+------------+---------+------------------+------------------------------+------------------+---------------+---------+
|     1      | task_03 | 09-06-2024 20:16 | Make laundry for next outing | 10-06-2024 08:00 | Not Completed |    No   |
|     2      | task_01 | 09-06-2024 20:08 |           Revision           | 10-06-2024 22:00 | Not Completed |    No   |
|     3      | task_02 | 09-06-2024 20:14 |     Refactor Kajola App      | 11-06-2024 09:00 | Not Completed |    No   |
+------------+---------+------------------+------------------------------+------------------+---------------+---------+

Do you want to continue? (y/n): n
```

## Author
- `Fawaz Abdganiyu` <fawazabdganiyu@gmail.com>
