def show_tasks(tasks):
    """Displays the current to-do list."""
    if not tasks:
        print("No tasks in the list.")
    else:
        print("To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task(tasks, task_name):
    """Adds a new task to the list."""
    tasks.append(task_name)
    print(f"Task '{task_name}' added.")

def delete_task(tasks, task_index):
    """Deletes a task from the list based on its index."""
    try:
        index = int(task_index) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            print(f"Task '{removed_task}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    """Main function to manage the to-do list."""
    tasks = []
    while True:
        print("\nOptions:")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            task_name = input("Enter the task: ")
            add_task(tasks, task_name)
        elif choice == '3':
            show_tasks(tasks)
            task_index = input("Enter the number of the task to delete: ")
            delete_task(tasks, task_index)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()