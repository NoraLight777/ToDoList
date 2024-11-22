def complete_task(tasks, task_id):
    """
    Marks a specific task as complete.
    
    Args:
        tasks (list): A list of tasks, where each task is a dictionary.
        task_id (int): The ID of the task to be marked as complete.

    Returns:
        list: The updated list of tasks.
    """
    if 0 < task_id <= len(tasks):
        task = tasks[task_id - 1]  # Adjust for zero-based indexing
        if not task["completed"]:
            task["completed"] = True
            print(f"Task '{task['name']}' has been marked as complete. ✔️")
        else:
            print(f"Task '{task['name']}' is already marked as complete.")
    else:
        print("Invalid task number. Please try again.")
    
    return tasks

