def add_task(tasks, task_name):
    task = {"id": len(tasks) + 1, "name": task_name, "completed": False}
    tasks.append(task)
    return tasks