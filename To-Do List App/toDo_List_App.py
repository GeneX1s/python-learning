# Simple To-Do List App

# List to store tasks
tasks = []

def add_task(task_name):
    """Adds a task to the to-do list."""
    tasks.append({"task": task_name, "completed": False})

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
        print(f"Task {task_number} marked as completed.")
    else:
        print("Invalid task number.")

def remove_task(task_number):
    """Removes a task from the list."""
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task['task']}' removed from the list.")
    else:
        print("Invalid task number.")

def main():
    """Main function to run the app."""
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
