import textwrap

class Menu:
    @staticmethod
    def display():
        menu_text = f"""
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
        # dedent removes common leading whitespace from every line in `menu_text`
        print(textwrap.dedent(menu_text).strip())
