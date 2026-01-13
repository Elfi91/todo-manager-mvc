import json
import os
from project import Project
from task import Task

class Todolist:
    def __init__(self):
        self.projects: list[Project] = []

    def add_project(self, project: Project) -> None:
        self.projects.append(project)
    
    def get_projects_str(self) -> str:
        if not self.projects:
            return "No projects available."
        return "\n".join([str(p) for p in self.projects])

    def get_projects_length(self) -> int:
        return len(self.projects)

    def is_name_duplicate(self, name: str) -> bool:
        for p in self.projects:
            if p.get_project_name().lower() == name.strip().lower():
                return True
        return False

    def update_project_name(self, project: Project, new_name: str) -> bool:
        new_name_strip = new_name.strip()
        new_name_lower = new_name_strip.lower()

        if new_name_lower == project.get_project_name().lower():
            # Functionality Explanation: If the new name only differs by case (e.g. "Work" -> "work"),
            # we allow the update directly to preserve the user's preferred casing without checking for duplicates.
            project.set_project_name(new_name_strip)
            return True
        
        if not self.is_name_duplicate(new_name_strip):
            # Functionality Explanation: For a completely new name, we must first verify that no other project
            # already uses this name to maintain uniqueness constraints.
            project.set_project_name(new_name_strip)
            return True
        return False
    
    def remove_project(self, project: Project) -> None:
        if project in self.projects:
            self.projects.remove(project)
    
    def save_to_json(self, filename="data.json"):
        data = [p.to_dict() for p in self.projects]
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print("Data saved successfully")

    def load_from_json(self, filename="data.json"):
        if not os.path.exists(filename):
            return
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                
            self.projects = []
            for p_data in data:
                # Functionality Explanation: Reconstruct the Project object from the dictionary data.
                project = Project(p_data["name"])
                project.id = p_data["id"] 
                for t_data in p_data["task_list"]:
                    # Functionality Explanation: Reconstruct each Task object and re-establish the relationship with its parent Project.
                    task = Task(t_data["title"])
                    task.id = t_data["id"]
                    task.completed = t_data["completed"]
                    project.add_task(task)
                self.add_project(project)
        except Exception as e:
            print(f"Error loading data: {e}")