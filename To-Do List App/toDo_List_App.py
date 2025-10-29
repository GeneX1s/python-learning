import json
import os

# File where tasks will be saved
TASKS_FILE = "tasks.json"

# List to store tasks
tasks = []

def load_tasks():
    """Loads tasks from the JSON file if it exists, otherwise creates an empty file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    else:
        # If the file doesn't exist, create an empty one
        with open(TASKS_FILE, "w") as file:
            json.dump([], file, indent=4)
        return []  # Return an empty list if the file was just created

def save_tasks():
    """Saves the current tasks to the JSON file."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(task_name):
    """Adds a task to the to-do list."""
    tasks.append({"task": task_name, "completed": False})
    save_tasks()  # Persist the data

def view_tasks():
    """Displays all tasks in the list."""
    if len(tasks) == 0:
        print("No tasks in the list.")
    else:
        print("\n--- To-Do List ---")
        for idx, task in enumerate(tasks, 1):
            status = "Done" if task["completed"] else "Pending"
            print(f"{idx}. {task['task']} [{status}]")

def mark_done(task_number):
    """Marks a task as completed."""
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        save_tasks()  # Persist the data
        print(f"Task {task_number} marked as completed.")
    else:
        print("Invalid task number.")

def remove_task(task_number):
    """Removes a task from the list."""
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks()  # Persist the data
        print(f"Task '{removed_task['task']}' removed from the list.")
    else:
        print("Invalid task number.")

def main():
    """Main function to run the app."""
    global tasks
    tasks = load_tasks()  # Load tasks from the file when the app starts

    print("Welcome to your To-Do List App!")
    
    while True:
        print("\nChoose an option:")
        print("1. Add a task")
        print("2. View all tasks")
        print("3. Mark a task as completed")
        print("4. Remove a task")
        print("5. Exit")
        
        choice = input("Enter the number of your choice: ")
        
        if choice == '1':
            task_name = input("Enter the task name: ")
            add_task(task_name)
            print(f"Added task: '{task_name}'")
        
        elif choice == '2':
            view_tasks()
        
        elif choice == '3':
            try:
                task_number = int(input("Enter the task number to mark as completed: "))
                mark_done(task_number)
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == '4':
            try:
                task_number = int(input("Enter the task number to remove: "))
                remove_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == '5':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please choose a valid option.")

# Run the app
if __name__ == "__main__":
    main()
