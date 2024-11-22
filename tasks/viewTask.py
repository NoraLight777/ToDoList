def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for idx, task in enumerate(tasks, start=1):
            status = "✔️" if task["completed"] else "❌"
            print(f"{idx}. {task['name']} [{status}]")
