from project import Project

class Todolist:
    def __init__(self):
        self.projects: list[Project] = []

    def add_project(self, project: Project) -> None:
        self.projects.append(project)
    
    def get_projects_str(self) -> str:
        if not self.projects:
            return "Nessun progetto presente."
        return "\n".join([str(p) for p in self.projects])

    def get_projects_length(self) -> int:
        return len(self.projects)

    def find_project_by_id(self, project_id: str) -> Project:
        return next((p for p in self.projects if p.get_project_id() == project_id), None)

    def is_name_duplicate(self, name: str) -> bool:
        for p in self.projects:
            if p.get_project_name().lower() == name.strip().lower():
                return True
        return False

    def update_project_name(self, project_id: str, new_name: str) -> bool:
        project = self.find_project_by_id(project_id)
        if project:
            project.set_project_name(new_name)
            return True
        return False