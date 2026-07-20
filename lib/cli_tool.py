# cli_tool.py

import argparse
from models import Task, User

# Global dictionary to store users and their tasks
users = {}

def add_task(args):
     # Check if the user exists, if not, create one
    user = users.get(args.user)
    if user is None:
        user = User(args.user)
        users[args.user] = user

     # Create a new Task with the given title
    task = Task(args.title)
    user.add_task(task)

def complete_task(args):
    # Look up the user by name
    user = users.get(args.user)

    if user:
        for task in user.tasks:
            # Look up the task by title
            if task.title == args.title:
                # Mark the task as complete
                task.complete()
                return
        print("❌ Task not found.")
    else:
        print("❌ User not found.")


# CLI entry point
def main():
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers()

    # Subparser for adding tasks
    add_parser = subparsers.add_parser("add-task", help="Add a task for a user")
    add_parser.add_argument("user")
    add_parser.add_argument("title")
    add_parser.set_defaults(func=add_task)

    # Subparser for completing tasks
    complete_parser = subparsers.add_parser("complete-task", help="Complete a user's task")
    complete_parser.add_argument("user")
    complete_parser.add_argument("title")
    complete_parser.set_defaults(func=complete_task)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()