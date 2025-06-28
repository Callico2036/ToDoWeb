class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "✔" if self.completed else "✘"
        return f"[{status}] {self.title} - {self.description}"


class DeadlineTask(Task):
    def __init__(self, title, description, deadline):
        super().__init__(title, description)
        self.deadline = deadline

    def __str__(self):
        status = "✔" if self.completed else "✘"
        return f"[{status}] {self.title} (Deadline: {self.deadline}) - {self.description}"


class DailyTask(Task):
    def __init__(self, title, description, day):
        super().__init__(title, description)
        self.day = day

    def __str__(self):
        status = "✔" if self.completed else "✘"
        return f"[{status}] {self.title} (Every: {self.day}) - {self.description}"
