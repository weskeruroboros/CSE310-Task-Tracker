"""
CSE 310 - Module #1 Project
Author: Student
Description: A task and study tracker application that allows users to manage 
             coursework tasks, set priorities, view summaries, and save data to JSON.
"""

import json
import os
from datetime import datetime


def display_welcome():
    """
    Prints the initial welcome message to verify system execution.
    """
    print("\n==========================================")
    print("Hello World! Welcome to CSE 310.")
    print("==========================================\n")


def load_tasks(filename="tasks.json"):
    """
    Loads saved tasks from a local JSON file.
    Returns a list of task dictionaries, or an empty list if no file exists.
    """
    if os.path.exists(filename):
        try:
            with open(filename, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("[Warning] Could not read task file. Starting with a fresh list.")
    return []


def save_tasks(tasks, filename="tasks.json"):
    """
    Saves the current list of tasks to a local JSON file.
    """
    try:
        with open(filename, "w") as file:
            json.dump(tasks, file, indent=4)
        print("[Saved] Tasks saved successfully.")
    except IOError as err:
        print(f"[Error] Failed to save tasks: {err}")


def add_task(tasks):
    """
    Prompts the user for task details (title, category, estimated hours)
    and appends a new task record to the task list.
    """
    print("--- Add New Course Task ---")
    title = input("Enter task title/description: ").strip()
    if not title:
        print("[Error] Task title cannot be blank.\n")
        return

    category = input("Enter category (e.g., CSE 310, Reading, Project): ").strip()
    if not category:
        category = "General"

    try:
        hours = float(input("Enter estimated completion hours: "))
        if hours <= 0:
            print("[Error] Hours must be greater than zero.\n")
            return
    except ValueError:
        print("[Error] Invalid number format.\n")
        return

    new_task = {
        "id": len(tasks) + 1,
        "title": title,
        "category": category,
        "hours": hours,
        "status": "Pending",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    tasks.append(new_task)
    print(f"[Success] Added '{title}' under {category}.\n")


def view_all_tasks(tasks):
    """
    Displays a formatted list of all current tasks and their details.
    """
    print("--- Current Task List ---")
    if not tasks:
        print("No tasks available.\n")
        return

    print(f"{'ID':<4} | {'Category':<12} | {'Title':<25} | {'Hours':<6} | {'Status':<10}")
    print("-" * 68)
    for task in tasks:
        print(f"{task['id']:<4} | {task['category']:<12} | {task['title']:<25} | {task['hours']:<6.1f} | {task['status']:<10}")
    print()


def mark_task_complete(tasks):
    """
    Prompts the user for a task ID and updates that task's status to Completed.
    """
    print("--- Mark Task Complete ---")
    if not tasks:
        print("No tasks available to complete.\n")
        return

    try:
        task_id = int(input("Enter the ID of the completed task: "))
        for task in tasks:
            if task["id"] == task_id:
                task["status"] = "Completed"
                print(f"[Updated] Task '{task['title']}' is now Completed!\n")
                return
        print("[Error] Task ID not found.\n")
    except ValueError:
        print("[Error] Please enter a valid numerical ID.\n")


def display_summary(tasks):
    """
    Calculates total tasks, completed count, and total estimated study hours.
    """
    print("--- Task Progress Summary ---")
    if not tasks:
        print("No tasks available for summary.\n")
        return

    total_tasks = len(tasks)
    completed = sum(1 for t in tasks if t["status"] == "Completed")
    total_hours = sum(t["hours"] for t in tasks)

    print(f"Total Tasks:     {total_tasks}")
    print(f"Completed Tasks: {completed}")
    print(f"Pending Tasks:   {total_tasks - completed}")
    print(f"Total Hours:     {total_hours:.1f} hrs\n")


def show_menu():
    """
    Prints the main user interface menu options.
    """
    print("Select an option:")
    print("1. Add New Task")
    print("2. View All Tasks")
    print("3. Mark Task as Complete")
    print("4. View Progress Summary")
    print("5. Save and Exit")


def main():
    """
    Main application loop controlling menu execution and program flow.
    """
    display_welcome()
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Enter choice (1-5): ").strip()
        print()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_all_tasks(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            display_summary(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye!\n")
            break
        else:
            print("[Error] Invalid selection. Choose a number between 1 and 5.\n")


if __name__ == "__main__":
    main()