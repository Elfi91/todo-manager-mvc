import uuid

class Project:
    def __init__(self, name: str):
        self.id = str(uuid.uuid4())
        self.name = name
        self.task_list = []

    def get_project_id(self) -> str:
        return self.id

    def get_project_name(self) -> str:
        return self.name
    
    def set_project_name(self, new_name: str) -> None:
        self.name = new_name

    def add_task(self, task) -> None:
        self.task_list.append(task)

    def is_task_already_existing(self, task_title: str) -> bool:
        for t in self.task_list:
            if t.title.strip().lower() == task_title.strip().lower():
                return True
        return False

    def get_tasks_str(self) -> str:
        if not self.task_list:
            return "Nessuna task presente in questo progetto."
        return "\n".join([str(t) for t in self.task_list])

    def __str__(self) -> str:
        return f"ID: {self.id} | Nome: {self.name} ({len(self.task_list)} task)"