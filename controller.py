from todolist import Todolist
from project import Project
from task import Task

class TodoController:
    def __init__(self, todo: Todolist):
        self.todo = todo

    def handle_add_project(self):
        print("\n" + "="*40)
        print("  ➕  NEW PROJECT")
        print("="*40)
        name = input("Project name: ").strip()
        if not name:
            print("❌ Error: The name cannot be empty.")
            return
        if self.todo.is_name_duplicate(name):
            print(f"❌ Error: Project '{name}' already exists.")
        else:
            self.todo.add_project(Project(name))
            self.todo.save_to_json()
            print(f"✅ Project '{name}' created successfully.")

    def handle_add_task(self):
        print("\n" + "="*40)
        print("  📝  NEW TASK")
        print("="*40)
        project = self._select_project()
        if project:
            print(f"\n📍 Selected project: {project.get_project_name()}")
            title = input("Task title: ").strip()
            if not title:
                print("❌ Error: The title cannot be empty.")
                return
            if project.is_task_already_existing(title):
                print("❌ Error: Task already exists in the project.")
            else:
                project.add_task(Task(title))
                self.todo.save_to_json()
                print("✅ Task added successfully!")

    def handle_list_projects(self):
        print("\n" + "="*40)
        print("  📂  PROJECT LIST")
        print("="*40)
        print(self.todo.get_projects_str())

    def handle_list_tasks(self):
        project = self._select_project()
        if project:
            print(f"\n📋 Tasks for project '{project.get_project_name()}':")
            print(project.get_tasks_str())

    def handle_edit_project(self):
        project = self._select_project()
        if project:
            new_n = input(f"New name for '{project.get_project_name()}' (or 'cancel'): ").strip()
            if new_n and new_n.lower() != 'cancel':
                if self.todo.update_project_name(project, new_n):
                    self.todo.save_to_json()
                    print("✅ Name updated successfully.")
                else:
                    print("❌ Error: A project with this name already exists.")

    def handle_delete_project(self):
        print("\n" + "="*40)
        print("  🗑️   DELETE PROJECT")
        print("="*40)
        project = self._select_project()
        if project:
            confirm = input(f"❗ Are you sure you want to delete '{project.get_project_name()}' and all its tasks? (y/n): ").strip().lower()
            if confirm == 'y':
                self.todo.remove_project(project)
                self.todo.save_to_json()
                print("✅ Project deleted.")
            else:
                print("🚫 Operation cancelled.")

    def handle_delete_task(self):
        print("\n" + "="*40)
        print("  ❌  DELETE TASK")
        print("="*40)
        project = self._select_project()
        if project:
            if not project.task_list:
                print("ℹ️  No tasks in this project.")
                return
            
            for i, task in enumerate(project.task_list, start=1):
                print(f"{i}. {task}")
            
            try:
                choice = int(input("\nNumber of task to delete (0 to cancel): "))
                if choice != 0 and 0 < choice <= len(project.task_list):
                    # FAdjust the user's input (1-based index) to match Python's list indexing (0-based)
                    # to correctly retrieve the selected task object.
                    task_to_remove = project.task_list[choice-1]
                    project.remove_task(task_to_remove)
                    self.todo.save_to_json()
                    print("✅ Task removed successfully.")
                else:
                    print("🚫 Operation cancelled.")
            except ValueError:
                print("⚠️  Please enter a valid number.")

    def handle_complete_task(self):
        project = self._select_project()
        if project:
            tasks_to_do = [t for t in project.task_list if not t.completed]
            if not tasks_to_do:
                print("🎉 All tasks have been completed!")
                return
            for i, task in enumerate(tasks_to_do, start=1):
                print(f"{i}. {task}")
            try:
                choice = int(input("\nNumber of task to complete (0 to cancel): "))
                if choice != 0 and 0 < choice <= len(tasks_to_do):
                    tasks_to_do[choice-1].mark_as_completed()
                    self.todo.save_to_json()
                    print("✅ Task completed successfully!")
            except ValueError:
                print("⚠️  Please enter a valid number.")

    def _select_project(self):
        projects = self.todo.projects
        if not projects:
            print("⚠️  No projects available.")
            return None
        for i, project in enumerate(projects, start=1):
            print(f"{i}. {project.get_project_name()}")
        try:
            choice = int(input("\nChoose the number (0 to cancel): "))
            if 0 < choice <= len(projects):
                return projects[choice-1]
        except ValueError:
            pass
        return None