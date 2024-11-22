def edit_task(tasks, task_id, new_name):
    """
    Edits the name of a specific task.

    Args:
        tasks (list): A list of tasks, where each task is a dictionary.
        task_id (int): The ID of the task to edit.
        new_name (str): The new name for the task.

    Returns:
        list: The updated list of tasks.
    """
    if 0 < task_id <= len(tasks):
        task = tasks[task_id - 1]  # Adjust for zero-based indexing
        old_name = task["name"]
        task["name"] = new_name
        print(f"Task '{old_name}' has been updated to '{new_name}'.")
