Task Tracker CLI 🚀
A simple command-line tool to track your tasks efficiently.

📖 Overview
This Task Tracker CLI allows users to manage their tasks via the terminal. Users can add, update, delete, and list tasks, as well as mark them as to-do, in-progress, or done. Tasks are stored in a JSON file.

🎯 Features
✅ Add new tasks
✅ Update or delete tasks
✅ Mark tasks as to-do, in-progress, or done
✅ List all tasks or filter by status

🛠️ Installation & Setup
1️⃣ Clone the repository

sh
Copy
Edit
git clone https://github.com/XIUXIU25/task_tracker.git
cd task_tracker
2️⃣ Run the script
Make sure you have Python 3 installed. Run the command:

sh
Copy
Edit
python task_tracker.py <command> [arguments]
🚀 Usage
Adding a Task
sh
Copy
Edit
python task_tracker.py add
(You will be prompted to enter a task description.)

Updating a Task
sh
Copy
Edit
python task_tracker.py update <task_id> "<new_description>"
Deleting a Task
sh
Copy
Edit
python task_tracker.py delete <task_id>
Marking a Task as Done or In Progress
sh
Copy
Edit
python task_tracker.py mark-done <task_id>
python task_tracker.py mark-in-progress <task_id>
Listing Tasks
List all tasks:
sh
Copy
Edit
python task_tracker.py list
List tasks by status:
sh
Copy
Edit
python task_tracker.py list done
python task_tracker.py list todo
python task_tracker.py list in-progress
🛑 Error Handling
If a task ID does not exist, the program will display an appropriate error message.
If the JSON file is empty or corrupted, it will be reinitialized.
📜 License
This project is licensed under the MIT License.