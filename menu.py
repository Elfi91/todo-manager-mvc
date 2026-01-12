import textwrap

class Menu:
    @staticmethod
    def display():
        testo_menu = f"""
        {"="*35}
                TODO MANAGER
        {"="*35}
        1. Aggiungi Progetto
        2. Elenca Progetti 
        3. Modifica Nome Progetto 
        4. Rimuovi Progetto
        5. Aggiungi Task
        6. Elenca Task
        7. Completa Task
        8. Rimuovi Task
        9. Esci
        {"="*35}
        """
        print(textwrap.dedent(testo_menu).strip())
