import textwrap

class Menu:
    @staticmethod
    def display():
        testo_menu = f"""
        {"="*40}
                🚀 TODO LIST MANAGER
        {"="*40}
        
        📁 PROGETTI
          [1] Aggiungi Progetto
          [2] Elenca Progetti
          [3] Rinomina Progetto
          [4] Rimuovi Progetto

        📝 TASKS
          [5] Aggiungi Task
          [6] Elenca Task
          [7] Completa Task
          [8] Rimuovi Task

        ⚙️  SISTEMA
          [9] Esci e Salva
        {"="*40}
        """
        print(textwrap.dedent(testo_menu).strip())
