# Todo Manager OOP 📝

Un gestore di attività (To-Do List) sviluppato in Python seguendo i principi della **Programmazione a Oggetti (OOP)** e il pattern **MVC (Model-View-Controller)**.

## 🎮 Tabella dei Comandi

N° | Comando | Azione | Descrizione |
| :--- | :--- | :--- | :--- |
| **[1]** | **`Add Project`** | **Aggiungi Progetto** | Valida il nome, controlla i duplicati e crea un nuovo progetto nel database |
| **[2]** | **`List Projects`** | **Mostra Progetti** | Visualizza l'elenco completo dei progetti con il relativo conteggio delle task |
| **[3]** | **`Edit`** | **Rinomina** | Avvia la procedura guidata per cambiare il nome a un progetto esistente |
| **[4]** | **`Delete Project`** | **Rimuovi Progetto** | Elimina definitivamente un progetto e tutte le sue task |
| **[5]** | **`Add task`** | **Aggiungi Task** | Permette di aggiungere una nuova attività specifica all'interno di un progetto scelto |
| **[6]** | **`List Tasks`** | **Mostra Tasks** | Visualizza tutte le attività (✅ e ❌) associate a un singolo progetto |
| **[7]** | **`Complete`** | **Completa Task** | Mostra le task da fare (❌) e permette di segnarle come completate (✅) |
| **[8]** | **`Delete Task`** | **Rimuovi Task** | Elimina una singola attività da un progetto |
| **[9]** | **`Exit`** | **Esci** | Chiude l'applicazione in modo sicuro salvando i dati aggiornati su JSON |

## 🚀 Funzionalità

- **Persistenza Dati**: Salvataggio e caricamento automatico tramite file `data.json`.
- **Gestione Progetti**: Crea, elenca e rinomina progetti (case-insensitive).
- **Gestione Task**: Aggiungi attività ai progetti e segnale come completate.
- **Interfaccia Pulita**: Visualizzazione intuitiva con icone (✅/❌) e senza ID tecnici superflui.
- **Validazione**: Controllo dei duplicati e gestione degli input vuoti.

## 📂 Struttura del Progetto
Il progetto segue il pattern architetturale **MVC**:
#### 📦 Modelli (Data Management)
- **`project.py`**: Definisce l'oggetto Progetto e la sua logica interna
- **`task.py`**: Definisce l'oggetto Task e i relativi stati (✅/❌)
- **`todolist.py`**: Gestisce l'intera collezione di progetti e la persistenza su file JSON

#### 🖥️ Vista (User Interface)
- **`menu.py`**: Gestisce esclusivamente la visualizzazione del menu nel terminale

#### ⚙️ Controller (Business Logic)
- **`controller.py`**: Il "cervello" dell'app che coordina le azioni tra l'utente e i modelli

#### 🚀 Entry Point
- **`main.py`**: Punto di avvio dell'applicazione e gestione del ciclo di esecuzione

## 🛠️ Requisiti

- Python 3.10 o superiore
- Nessuna libreria esterna richiesta (utilizza solo moduli standard come `json`, `os`, `uuid` e `textwrap`)

## 💻 Installazione e Utilizzo

1. Clona la cartella del progetto.
2. Apri il terminale nella cartella del progetto
3. Avvia l'applicazione
## ⚠️ Note sull'utilizzo
- **Salvataggio automatico:** Ogni modifica viene salvata istantaneamente nel file `data.json`.
- **Input pulito:** Il sistema gestisce automaticamente gli spazi bianchi accidentali negli input.
- **Chiusura sicura:** Puoi chiudere il programma tramite il comando 9 o premendo `Ctrl+C`; il sistema gestirà l'interruzione senza mostrare errori di sistema.

## 📜 Licenza
Questo progetto è distribuito sotto la licenza MIT. Consulta il file [LICENSE](LICENSE) per ulteriori dettagli
