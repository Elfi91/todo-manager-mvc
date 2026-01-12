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
                print("="*30)
                print("  --- Aggiungi progetto ---")
                print("="*30)
                project_name = input("Inserisci nome del progetto: ")
                if todolist.is_project_name_already_existing(project_name):
                    print(f"Un oggetto con il nome {project_name} esiste già")
                    continue
                
                new_project = Project(project_name)
                todolist.add_project(new_project)
                print(f"Il numero di progetti è: {todolist.get_projects_lenght()}")
                continue

            case "2":
                print("="*30)
                print("  --- Aggiungi task ---")
                print("="*30)
                continue

            case "3": 
                print("="*30)
                print("  --- Aggiungi tag ---")
                print("="*30)
                continue

            case "4": 
                print("="*30)
                print("  --- Lista Progetti ---")
                print("="*30)
                print(todolist.get_projects())

            case "5":
                print("="*30)
                print("  --- Lista le tasks ---")
                print("="*30)
                continue
            
            case "6":
                print("="*30)
                print("  --- Lista i tags ---")
                print("="*30)
                continue

            case "7":
                print("="*30)
                print("--- Modifica nome progetto ---")
                print("="*30)
                print(todolist.get_projects())

                id_progetto = input("Inserisci l'id del progetto da aggiornare: ")

                while True:

                    new_name = input("Inserisci il nuovo nome del progetto: ")

                    if todolist.is_project_name_already_existing(new_name):
                        print(f"Un oggetto con il nome {new_name} esiste già")
                        continue

                    todolist.update_project_name(id_progetto, new_name)
                    print(f"Update eseguito con successo per l'oggetto {id_progetto}")
                    break
                continue

            case "8":
                print("="*30)
                print("  --- Arrivederci ---")
                print("="*30)
                break

            case _: 
                print("Inserisci un numero da 1 a 8")
                continue

if __name__ == "__main__":
    main()