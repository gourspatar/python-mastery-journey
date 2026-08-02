class TodoManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if not task:
            raise ValueError("Task cannot be empty.")

        if any(t["name"] == task for t in self.tasks):
            raise ValueError("Task already exists.")

        self.tasks.append({
            "name": task,
            "completed": False
        })

    def remove_task(self, task):
        for t in self.tasks:
            if t["name"] == task:
                self.tasks.remove(t)
                return

        raise ValueError("Task not found.")

    def mark_completed(self, task):
        for t in self.tasks:
            if t["name"] == task:
                t["completed"] = True
                return

        raise ValueError("Task not found.")

    def pending_tasks(self):
        return [
            t["name"]
            for t in self.tasks
            if not t["completed"]
        ]