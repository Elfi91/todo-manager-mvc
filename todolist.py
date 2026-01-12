from project import Project


class Todolist:
    def __init__(self):
        self.projects: list[Project] = []

    def add_project(self, project: Project) -> None:
        self.projects.append(project)
    
    def get_projects_lenght(self) -> int:
        return len(self.projects)

    def get_projects(self) -> list[Project]:
        if not self.projects:
            return "Lista vuota."
    
        risultato = "" # Inizializza la stringa
        for p in self.projects:
            risultato += f"{p.id} - {p.name}\n"
        return risultato

    def is_project_name_already_existing(self, new_name: str) -> bool:
        for p in self.projects:
            if p.get_project_name() == new_name.strip():
                return True
        return False
        
    def update_project_name(self, id: str, new_name: str) -> None:
        project = next((project for project in self.projects if project.get_project_id() == id), None)
        
        if project:
            project.set_project_name(new_name)
        else:
            print(f"errore: Nessun progetto trovato con l'ID {id}")
        

