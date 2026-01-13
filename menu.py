import textwrap

class Menu:
    @staticmethod
    def display():
        testo_menu = f"""
        {"="*40}
                🚀 TODO LIST MANAGER
        {"="*40}
        
        📁 PROJECTS
          [1] Add Project
          [2] List Projects
          [3] Rename Project
          [4] Remove Project

        📝 TASKS
          [5] Add Task
          [6] List Tasks
          [7] Complete Task
          [8] Remove Task

        ⚙️  SYSTEM
          [9] Exit and Save
        {"="*40}
        """
        print(textwrap.dedent(testo_menu).strip())
