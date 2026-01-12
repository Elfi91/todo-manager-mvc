

from project import Project


class Todolist:
    def __init__(self):
        self.projects = []

    def add_project(self, project: Project) -> None:
        self.projects.append(project)
    
    def get_projects_lenght(self) -> int:
        return len(self.projects)

    def get_projects(self) -> list[Project]:
        if not self.projects:
            return "Lista vuota."
        
        risultato = ""
        for p in self.projects:
            risultato += f"{p.id} - {p.name}\n"
        return risultato
        
    def update_project_name(self, id: str, nuovo_nome: str) -> str:
        target = next((project for project in self.projects if project.get_project_id() == id), None)
        if target:
            target.set_project_name(nuovo_nome)
            return f"Successo! Il nuovo nome del progetto è: {target.get_project_name()}"
        else:
            return "Errore: progetto non trovato"
