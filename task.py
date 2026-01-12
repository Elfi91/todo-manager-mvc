import uuid

class Task:
    def __init__(self, title: str):
        self.id = str(uuid.uuid4())
        self.title = title
        self.completed = False

    def mark_as_completed(self) -> None:
        self.completed = True

    def __str__(self) -> str:
        status = "✅" if self.completed else "❌"
        return f"[{status}] ID: {self.id} | Titolo: {self.title}"