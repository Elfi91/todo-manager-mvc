from todolist import Todolist
from menu import Menu
from controller import TodoController

def main():
    todo = Todolist()
    todo.load_from_json()
    ctrl = TodoController(todo)
    menu = Menu()

    while True:
        menu.display()
        choice = input("Seleziona l'operazione: ").strip()

        match choice:
            case "1": 
                ctrl.handle_add_project()
            case "2": 
                ctrl.handle_list_projects()
            case "3":
                ctrl.handle_edit_project()
            case "4": 
                ctrl.handle_delete_project()            
            case "5": 
                ctrl.handle_add_task()
            case "6": 
                ctrl.handle_list_tasks()
            case "7":
                ctrl.handle_complete_task()
            case "8": 
                ctrl.handle_delete_task()        
            case "9":
                todo.save_to_json()
                print("\nArrivederci!")
                break
            case _:
                print("\nScelta non valida (1-9)")

if __name__ == "__main__":
    try:
       main()
    except KeyboardInterrupt: 
        print("\nProgramma interrotto manualmente Arrivederci")