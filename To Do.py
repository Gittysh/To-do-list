# Store tasks
to_do = []

# Function to display the menu
def show_menu():
    print("\nTo-Do List Menu:")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Exit")

# Function to display all tasks
def view_tasks():
    if not to_do:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

# Function to add a new task
def add_task():
    task = input("\nEnter a new task: ")
    to_do.append(task)
    print(f"Task '{task}' added successfully!")

# Function to remove a task
def remove_task():
    view_tasks()
    if to_do:
        try:
            task_number = int(input("\nEnter the number of the task to remove: "))
            if 1 <= task_number <= len(to_do):
                removed_task = to_do.pop(task_number - 1)
                print(f"Task '{removed_task}' removed successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

# Main program loop
while True:
    show_menu()
    choice = input("\nChoose an option (1-4): ")
    
    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Exiting the To-Do List program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a number between 1 and 4.")
