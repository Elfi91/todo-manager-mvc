from todolist import Todolist
from menu import Menu
from controller import TodoController

def main():
    todo = Todolist()
    ctrl = TodoController(todo)
    menu = Menu()

    while True:
        menu.display()
        choice = input("Seleziona l'operazione da eseguire: ")

        match choice:
            case "1": ctrl.handle_add_project()
            case "2": ctrl.handle_add_task()
            case "4": ctrl.handle_list_projects()
            case "5": ctrl.handle_list_tasks()
            case "7": ctrl.handle_edit_project()
            case "8": 
                print("\nChiusura del programma... Arrivederci!")
                break
            case _: 
                print("\nScelta non valida. Inserisci un numero da 1 a 8.")

if __name__ == "__main__":
    main()