# # Lesson 7 - Personal Planner

# ## Task 1: Display a Menu
# **Create a menu-driven system that lets the user choose actions for the task list program.​**

# Start the program by displaying a menu with the following options:​
# - Create a new task file ​
# - View all tasks.​
# - Add a new task.​
# - Delete a task.​
# - Mark a task as done.​
# - Exit the program.​

# Prompt the user to input their choice by entering the corresponding number.

def display_menu():
    print("Menu:")
    print("1. Create a new task file")
    print("2. View all tasks")
    print("3. Add a new task")
    print("4. Mark a task as done")
    print("5. Delete a task")
    print("6. Exit the program")

# ## Task 2: Create a new task file
# **Initialize a new file for tasks and write a title to the file.​**

# Check if tasks.txt already exists:​
# - If the file exists, notify the user and ask if they want to overwrite it.​
# - If the file doesn’t exist, create the file and write "My Task List" as the title.​
# Confirm the creation of the file.
import os
def create_task_file():
    if os.path.exists("tasks.txt"):
        overwrite = input("tasks.txt already exists. Do you want to overwrite it? (yes/no): ")
        if overwrite.lower() != "yes":
            print("File creation cancelled.")
            return
    with open("tasks.txt", "w") as file:
        file.write("My Task List\n")
    print("tasks.txt has been created with the title 'My Task List'.")

# ## Task 3: View all tasks
# **Display all tasks from the file.​**

# Open tasks.txt and read its contents.​
# - Display tasks with numbering.​
# - If no tasks are found (i.e., only the title exists), display "No tasks found!".

def view_tasks():
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
    if len(tasks) <= 1:
        print("No tasks found!")
    else:
        for i, task in enumerate(tasks[1:], start=1):
            print(f"{i}. {task.strip()}")

# ## Task 4: Add a new task
# **Append new tasks to the file​**

# Prompt the user to input a new task.​
# - Append the task to tasks.txt without overwriting the existing tasks.​
# - Confirm the task has been added.

def add_task():
    new_task = input("Enter a new task: ")
    with open("tasks.txt", "a") as file:
        file.write(new_task + "\n")
    print(f"Task '{new_task}' has been added.")

# ## Task 5: Mark a Task as “done”
# **Update a task to indicate completion.​**

# Display all tasks with numbers.​
# - Prompt the user to input the number of the task to mark as done.​
# - Update the task in the file to show it is completed (e.g., "Go for a run (Done)").​
# - Save the updated tasks back to the file.

def mark_task_done():
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
    if len(tasks) <= 1:
        print("No tasks found!")
        return
    for i, task in enumerate(tasks[1:], start=1):
        print(f"{i}. {task.strip()}")
    task_number = int(input("Enter the number of the task to mark as done: "))
    if 1 <= task_number < len(tasks):
        tasks[task_number] = tasks[task_number].strip() + " (Done)\n"
        with open("tasks.txt", "w") as file:
            file.writelines(tasks)
        print(f"Task '{tasks[task_number].strip()}' has been marked as done.")
    else:
        print("Invalid task number.")
# ## Task 6: Delete a Task
# **Remove a task from the file.​**

# Display all tasks with numbers.​
# - Prompt the user to input the number of the task to delete.​
# - Remove the selected task from the file.​
# - Save the updated tasks back to tasks.txt.

def delete_task():
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
    if len(tasks) <= 1:
        print("No tasks found!")
        return
    for i, task in enumerate(tasks[1:], start=1):
        print(f"{i}. {task.strip()}")
    task_number = int(input("Enter the number of the task to delete: "))
    if 1 <= task_number < len(tasks):
        deleted_task = tasks.pop(task_number)
        with open("tasks.txt", "w") as file:
            file.writelines(tasks)
        print(f"Task '{deleted_task.strip()}' has been deleted.")
    else:
        print("Invalid task number.")