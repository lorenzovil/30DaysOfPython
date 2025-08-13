import os
import json

FILENAME = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        json.dump(tasks, file)

# Show all tasks
def show_tasks(tasks):
    if not tasks:
        print("📂 No tasks yet.")
        return
    print("\n📋 Your Tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "✅" if task["done"] else "❌"
        print(f"{i}. {task['title']} [{status}]")

# Main program
tasks = load_tasks()

while True:
    print("\n=== To-Do List Menu ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")
    
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        title = input("Enter task name: ")
        tasks.append({"title": title, "done": False})
        save_tasks(tasks)
        print("✅ Task added!")

    elif choice == "2":
        show_tasks(tasks)

    elif choice == "3":
        show_tasks(tasks)
        num = input("Enter task number to mark as done: ")
        if num.isdigit() and 1 <= int(num) <= len(tasks):
            tasks[int(num)-1]["done"] = True
            save_tasks(tasks)
            print("✅ Task marked as done!")

    elif choice == "4":
        show_tasks(tasks)
        num = input("Enter task number to delete: ")
        if num.isdigit() and 1 <= int(num) <= len(tasks):
            tasks.pop(int(num)-1)
            save_tasks(tasks)
            print("🗑️ Task deleted!")

    elif choice == "5":
        print("👋 Goodbye!")
        break

    else:
        print("❌ Invalid option. Try again.")
