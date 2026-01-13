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
        # Functionality Explanation: textwrap.dedent handles the indentation of the multiline string.
        # It removes the common leading whitespace from each line so the menu prints correctly aligned to the left.
        print(textwrap.dedent(menu_text).strip())
