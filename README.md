# Todo Manager OOP 📝

A task manager (To-Do List) developed in Python following **Object-Oriented Programming (OOP)** principles and the **MVC (Model-View-Controller)** pattern.

## 🎮 Command Table

| N° | Command | Action | Description |
| :--- | :--- | :--- | :--- |
| **[1]** | **`Add Project`** | **Add Project** | Validates the name, checks for duplicates, and creates a new project in the database |
| **[2]** | **`List Projects`** | **List Projects** | Displays the full list of projects with their task count |
| **[3]** | **`Edit`** | **Rename** | Starts the wizard to rename an existing project |
| **[4]** | **`Delete Project`** | **Remove Project** | Permanently deletes a project and all its tasks |
| **[5]** | **`Add task`** | **Add Task** | Allows adding a new specific activity within a chosen project |
| **[6]** | **`List Tasks`** | **Show Tasks** | Displays all activities (✅ and ❌) associated with a single project |
| **[7]** | **`Complete`** | **Complete Task** | Shows tasks to do (❌) and allows marking them as completed (✅) |
| **[8]** | **`Delete Task`** | **Remove Task** | Deletes a single activity from a project |
| **[9]** | **`Exit`** | **Exit** | Safely closes the application saving updated data to JSON |

## 🚀 Features

- **Data Persistence**: Automatic saving and loading via `data.json` file.
- **Project Management**: Create, list, and rename projects (case-insensitive).
- **Task Management**: Add activities to projects and mark them as completed.
- **Clean Interface**: Intuitive display with icons (✅/❌) and without superfluous technical IDs.
- **Validation**: Duplicate check and empty input handling.

## 📂 Project Structure
The project follows the **MVC** architectural pattern:
#### 📦 Models (Data Management)
- **`project.py`**: Defines the Project object and its internal logic
- **`task.py`**: Defines the Task object and its states (✅/❌)
- **`todolist.py`**: Manages the entire collection of projects and persistence on JSON file

#### 🖥️ View (User Interface)
- **`menu.py`**: Exclusively manages the menu display in the terminal

#### ⚙️ Controller (Business Logic)
- **`controller.py`**: The "brain" of the app that coordinates actions between the user and models

#### 🚀 Entry Point
- **`main.py`**: Application entry point and execution cycle management

## 🛠️ Requirements

- Python 3.10 or higher
- No external libraries required (uses only standard modules like `json`, `os`, `uuid`, and `textwrap`)

## 💻 Installation and Usage

1. Clone the project folder.
2. Open terminal in the project folder.
3. Start the application:
   ```bash
   python main.py
   ```

## ⚠️ Usage Notes
- **Auto-save:** Every change is saved instantly to the `data.json` file.
- **Clean Input:** The system automatically handles accidental whitespaces in inputs.
- **Safe Exit:** You can close the program via command 9 or by pressing `Ctrl+C`; the system will handle the interruption without showing system errors.

## 📜 License
This project is distributed under the MIT license. See the [LICENSE](LICENSE) file for further details.
