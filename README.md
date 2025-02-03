# Task Tracker CLI 🚀  
https://roadmap.sh/projects/task-tracker

A simple command-line tool to efficiently track your tasks.

## 📖 Overview  
The Task Tracker CLI allows users to manage their tasks via the terminal.  
Users can **add, update, delete, and list tasks**, as well as mark them as **to-do, in-progress, or done**.  
Tasks are stored in a JSON file for persistence.

## 🎯 Features  
✅ Add new tasks  
✅ Update or delete tasks  
✅ Mark tasks as **to-do, in-progress, or done**  
✅ List all tasks or filter by status  

---

## 🛠️ Installation & Setup  

### Clone the Repository  
```sh
git clone https://github.com/XIUXIU25/task_tracker.git
cd task_tracker

### Run the Script
Make sure you have Python 3 installed, then run:
python task_tracker.py [arguments]

🚀 Usage
Adding a Task
python task_tracker.py add

Updating a Task
python task_tracker.py update <task_id> "<new_description>"

Deleting a Task
python task_tracker.py delete <task_id>

Marking a Task as Done or In Progress
python task_tracker.py mark-done <task_id>
python task_tracker.py mark-in-progress <task_id>

Listing Tasks
python task_tracker.py list

Filter tasks by status:
python task_tracker.py list done
python task_tracker.py list todo
python task_tracker.py list in-progress

🛑 Error Handling
If a task ID does not exist, an appropriate error message will be displayed.
If the JSON file is empty or corrupted, it will be reinitialized automatically.

📜 License
This project is licensed under the MIT License.