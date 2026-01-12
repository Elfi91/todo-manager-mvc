from todolist import Todolist
from project import Project
from task import Task

class TodoController:
    def __init__(self, todo: Todolist):
        self.todo = todo

    def handle_add_project(self):
        print("\n" + "="*30)
        print("  --- Aggiungi Progetto ---")
        print("="*30)
        name = input("Inserisci il nome del progetto: ")
        if self.todo.is_name_duplicate(name):
            print(f"Errore: Un progetto chiamato '{name}' esiste già.")
        else:
            self.todo.add_project(Project(name))
            print(f"Progetto creato. Totale progetti: {self.todo.get_projects_length()}")

    def handle_add_task(self):
        print("\n" + "="*30)
        print("  --- Aggiungi Task ---")
        print("="*30)
        print(self.todo.get_projects_str())
        pid = input("\nInserisci l'ID del progetto: ")
        project = self.todo.find_project_by_id(pid)
        
        if project:
            title = input("Titolo della nuova task: ")
            if project.is_task_already_existing(title):
                print("Errore: Questa task esiste già in questo progetto.")
            else:
                project.add_task(Task(title))
                print("Task aggiunta con successo!")
        else:
            print("Errore: ID Progetto non trovato.")

    def handle_list_projects(self):
        print("\n" + "="*30)
        print("  --- Lista Progetti ---")
        print("="*30)
        print(self.todo.get_projects_str())

    def handle_list_tasks(self):
        print("\n" + "="*30)
        print("  --- Lista Task di un Progetto ---")
        print("="*30)
        print(self.todo.get_projects_str())
        pid = input("\nInserisci l'ID del progetto: ")
        project = self.todo.find_project_by_id(pid)
        if project:
            print(f"\nProgetto: {project.get_project_name()}")
            print("-" * 20)
            print(project.get_tasks_str())
        else:
            print("Errore: Progetto non trovato.")

    def handle_edit_project(self):
        print("\n" + "="*30)
        print("  --- Modifica Nome Progetto ---")
        print("="*30)
        print(self.todo.get_projects_str())
        pid = input("\nInserisci ID del progetto da modificare: ")
        
        while True:
            new_n = input("Inserisci il nuovo nome: ")
            if self.todo.is_name_duplicate(new_n):
                print("Errore: Nome già occupato da un altro progetto.")
                continue
            
            if self.todo.update_project_name(pid, new_n):
                print("Nome aggiornato con successo.")
            else:
                print("Errore: ID non trovato.")
            break