import json
from tasks.add_task import add_task
from tasks.view_tasks import view_tasks
from tasks.filter_tasks import filter_tasks
from tasks.edit_task import edit_task
from tasks.complete_task import complete_task
from tasks.delete_task import delete_task

# File path for storing tasks
TASKS_FILE = "data/tasks.json"

# Load tasks from file
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Main menu
def main():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List Manager ---")
        print("1. Add a Task")
        print("2. View All Tasks")
        print("3. Filter Tasks")
        print("4. Edit a Task")
        print("5. Mark a Task as Complete")
        print("6. Delete a Task")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            task_name = input("Enter the task name: ")
            tasks = add_task(tasks, task_name)
            save_tasks(tasks)
            print("Task added successfully!")
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            filter_choice = input("View (1) Completed or (2) Incomplete tasks? ")
            filter_tasks(tasks, filter_choice)
        elif choice == "4":
            task_id = int(input("Enter the task number to edit: "))
            new_name = input("Enter the new task name: ")
            tasks = edit_task(tasks, task_id, new_name)
            save_tasks(tasks)
            print("Task updated successfully!")
        elif choice == "5":
            task_id = int(input("Enter the task number to mark as complete: "))
            tasks = complete_task(tasks, task_id)
            save_tasks(tasks)
            print("Task marked as complete!")
        elif choice == "6":
            task_id = int(input("Enter the task number to delete: "))
            tasks = delete_task(tasks, task_id)
            save_tasks(tasks)
            print("Task deleted successfully!")
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
