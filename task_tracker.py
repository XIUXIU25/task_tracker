import os
import json
import argparse
from datetime import datetime

TASK_FILE = "tasks.json"

class Task:
    def __init__(self, id, description, status="todo"):
        self.id = id
        self.description = description
        self.status = status
        self.created_at = datetime.now().isoformat()
        self.updated_at = self.created_at

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
        }

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r') as file:
            tasks_dict = json.load(file)
            # Convert dictionaries back to Task objects
            return [Task(task["id"], task["description"], task["status"]) for task in tasks_dict]
    else:
        return []

def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        # Convert Task objects to dictionaries
        json.dump([task.to_dict() for task in tasks], file, indent=4)

def find_task_by_id(tasks, task_id):
    return next((task for task in tasks if task.id == task_id), None)

def add_task(description):
    tasks = load_tasks()
    new_id = max([task.id for task in tasks], default=0) + 1
    task = Task(new_id, description)
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task.id})")

def update_task(task_id, new_description):
    tasks = load_tasks()
    task = find_task_by_id(tasks, task_id)
    if task:
        task.description = new_description
        task.updated_at = datetime.now().isoformat()
        save_tasks(tasks)
        print(f"Task {task_id} updated successfully")
    else:
        print(f"Task {task_id} not found")

def delete_task(task_id):
    tasks = load_tasks()
    task = find_task_by_id(tasks, task_id)
    if task:
        tasks.remove(task)
        save_tasks(tasks)
        print(f"Task {task_id} deleted successfully")
    else:
        print(f"Task {task_id} not found")

def mark_task_status(task_id, status):
    tasks = load_tasks()
    task = find_task_by_id(tasks, task_id)
    if task:
        task.status = status
        task.updated_at = datetime.now().isoformat()
        save_tasks(tasks)
        print(f"Task {task_id} marked as {status}")
    else:
        print(f"Task {task_id} not found")

def list_tasks(status=None):
    tasks = load_tasks()
    if status:
        tasks = [task for task in tasks if task['status'] == status]
    for task in tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, Created At: {task['createdAt']}, Updated At: {task['updatedAt']}")

def main():
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Add task
    subparsers.add_parser("add", help="Add a new task")
    
    # Update task
    update_parser = subparsers.add_parser("update", help="Update an existing task")
    update_parser.add_argument("id", type=int, help="Task ID")
    update_parser.add_argument("description", help="New task description")

    # Delete task
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="Task ID")

    # Mark task
    mark_parser = subparsers.add_parser("mark", help="Mark task status")
    mark_parser.add_argument("id", type=int, help="Task ID")
    mark_parser.add_argument("status", choices=["todo", "in-progress", "done"], help="Task status")

    # List tasks
    subparsers.add_parser("list", help="List all tasks")
    subparsers.add_parser("list-done", help="List done tasks")
    subparsers.add_parser("list-todo", help="List todo tasks")
    subparsers.add_parser("list-in-progress", help="List in-progress tasks")

    args = parser.parse_args()

    if args.command == "add":
        description = input("Enter task description: ")
        add_task(description)
    elif args.command == "update":
        update_task(args.id, args.description)
    elif args.command == "delete":
        delete_task(args.id)
    elif args.command == "mark":
        mark_task_status(args.id, args.status)
    elif args.command == "list":
        list_tasks()
    elif args.command == "list-done":
        list_tasks("done")
    elif args.command == "list-todo":
        list_tasks("todo")
    elif args.command == "list-in-progress":
        list_tasks("in-progress")

if __name__ == "__main__":
    main()
