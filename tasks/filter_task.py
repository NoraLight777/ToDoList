def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for idx, task in enumerate(tasks, start=1):
            status = "✔️" if task["completed"] else "❌"
            print(f"{idx}. {task['name']} [{status}]")

def filter_tasks(tasks, filter_choice):
    """
    Filters tasks based on the user's choice.
    
    Args:
        tasks (list): A list of tasks, where each task is a dictionary.
        filter_choice (str): "1" for completed tasks, "2" for incomplete tasks.

    Returns:
        None. Prints the filtered tasks.
    """
    if filter_choice == "1":
        # Filter completed tasks
        completed_tasks = [task for task in tasks if task.get("completed")]
        print("\n--- Completed Tasks ---")
        if completed_tasks:
            for idx, task in enumerate(completed_tasks, start=1):
                print(f"{idx}. {task['name']} ✔️")
        else:
            print("No completed tasks found.")
    elif filter_choice == "2":
        # Filter incomplete tasks
        incomplete_tasks = [task for task in tasks if not task.get("completed")]
        print("\n--- Incomplete Tasks ---")
        if incomplete_tasks:
            for idx, task in enumerate(incomplete_tasks, start=1):
                print(f"{idx}. {task['name']} ❌")
        else:
            print("No incomplete tasks found.")
    else:
        print("Invalid choice. Please enter 1 for completed tasks or 2 for incomplete tasks.")
