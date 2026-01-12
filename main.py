"""
- menu
- todolist
- project
- task
- tag
"""

from menu import Menu
from project import Project
from todolist import Todolist


def main():
    todolist = Todolist()

    menu = Menu()

    while True: 

        menu.printMenu()

        i = input("Seleziona l'operazione da eseguire: ")

        match i:
            case "1": 
                print("Hai scelto aggiungi progetto")
                print("="*20)
                project_name = input("Inserisci nome del progetto: ")
                new_project = Project(project_name)
                todolist.add_project(new_project)
                print(todolist.get_projects_lenght())
                continue

            case "2": 
                print("Aggiungi task")
                continue

            case "4":
                print("\n--- Aggiorna Nome Progetto ---")
                print("="*20)
                id_progetto = input("Inserisci l'ID del progetto da aggiornare: ")
                nuovo_nome = input("Inserisci il NUOVO nome per questo progetto: ")

                risultato = todolist.update_project_name(id_progetto, nuovo_nome)
                print(risultato)

            case "5":
                print("\n--- Lista Progetti ---")
                print("="*20)
                print(todolist.get_projects())
            case "8":
                break
            case _: 
                print("Inserisci un numero da 1 a 7")
                continue



if __name__ == "__main__":
    main()