from todolist import Todolist
from project import Project
from task import Task

class TodoController:
    def __init__(self, todo: Todolist):
        self.todo = todo

    def handle_add_project(self):
        print("\n" + "="*40)
        print("  ➕  NUOVO PROGETTO")
        print("="*40)
        name = input("Nome del progetto: ").strip()
        if not name:
            print("❌ Errore: Il nome non può essere vuoto.")
            return
        if self.todo.is_name_duplicate(name):
            print(f"❌ Errore: Il progetto '{name}' esiste già.")
        else:
            self.todo.add_project(Project(name))
            self.todo.save_to_json()
            print(f"✅ Progetto '{name}' creato con successo.")

    def handle_add_task(self):
        print("\n" + "="*40)
        print("  📝  NUOVA TASK")
        print("="*40)
        project = self._seleziona_progetto()
        if project:
            print(f"\n📍 Progetto selezionato: {project.get_project_name()}")
            title = input("Titolo della task: ").strip()
            if not title:
                print("❌ Errore: Il titolo non può essere vuoto.")
                return
            if project.is_task_already_existing(title):
                print("❌ Errore: Task già presente nel progetto.")
            else:
                project.add_task(Task(title))
                self.todo.save_to_json()
                print("✅ Task aggiunta con successo!")

    def handle_list_projects(self):
        print("\n" + "="*40)
        print("  📂  LISTA PROGETTI")
        print("="*40)
        print(self.todo.get_projects_str())

    def handle_list_tasks(self):
        project = self._seleziona_progetto()
        if project:
            print(f"\n📋 Task del progetto '{project.get_project_name()}':")
            print(project.get_tasks_str())

    def handle_edit_project(self):
        project = self._seleziona_progetto()
        if project:
            new_n = input(f"Nuovo nome per '{project.get_project_name()}' (o 'annulla'): ").strip()
            if new_n and new_n.lower() != 'annulla':
                if self.todo.update_project_name(project, new_n):
                    self.todo.save_to_json()
                    print("✅ Nome aggiornato con successo.")
                else:
                    print("❌ Errore: Un progetto con questo nome esiste già.")

    def handle_delete_project(self):
        print("\n" + "="*40)
        print("  🗑️   ELIMINA PROGETTO")
        print("="*40)
        project = self._seleziona_progetto()
        if project:
            conferma = input(f"❗ Sei sicuro di voler eliminare '{project.get_project_name()}' e tutte le sue task? (s/n): ").strip().lower()
            if conferma == 's':
                self.todo.remove_project(project)
                self.todo.save_to_json()
                print("✅ Progetto eliminato.")
            else:
                print("🚫 Operazione annullata.")

    def handle_delete_task(self):
        print("\n" + "="*40)
        print("  ❌  ELIMINA TASK")
        print("="*40)
        project = self._seleziona_progetto()
        if project:
            if not project.task_list:
                print("ℹ️  Non ci sono task in questo progetto.")
                return
            
            for i, task in enumerate(project.task_list, start=1):
                print(f"{i}. {task}")
            
            try:
                scelta = int(input("\nNumero task da eliminare (0 per annullare): "))
                if scelta != 0 and 0 < scelta <= len(project.task_list):
                    task_da_rimuovere = project.task_list[scelta-1]
                    project.remove_task(task_da_rimuovere)
                    self.todo.save_to_json()
                    print("✅ Task rimossa con successo.")
                else:
                    print("🚫 Operazione annullata.")
            except ValueError:
                print("⚠️  Inserisci un numero valido.")

    def handle_complete_task(self):
        project = self._seleziona_progetto()
        if project:
            tasks_da_fare = [t for t in project.task_list if not t.completed]
            if not tasks_da_fare:
                print("🎉 Tutte le task sono state completate!")
                return
            for i, task in enumerate(tasks_da_fare, start=1):
                print(f"{i}. {task}")
            try:
                scelta = int(input("\nNumero task da completare (0 per annullare): "))
                if scelta != 0 and 0 < scelta <= len(tasks_da_fare):
                    tasks_da_fare[scelta-1].mark_as_completed()
                    self.todo.save_to_json()
                    print("✅ Task completata con successo!")
            except ValueError:
                print("⚠️  Inserisci un numero valido.")

    def _seleziona_progetto(self):
        progetti = self.todo.projects
        if not progetti:
            print("⚠️  Nessun progetto disponibile.")
            return None
        for i, project in enumerate(progetti, start=1):
            print(f"{i}. {project.get_project_name()}")
        try:
            scelta = int(input("\nScegli il numero (0 per annullare): "))
            if 0 < scelta <= len(progetti):
                return progetti[scelta-1]
        except ValueError:
            pass
        return None