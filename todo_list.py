# This program manages a to-do list for school tasks.

# Function to display the menu and get user input
def display_menu():
    # Display the options for the user to choose from
    print("\n1. Add a task")  # Option to add a new task
    print("2. View tasks")  # Option to view all tasks
    print("3. Remove a task")  # Option to remove a task by its number
    print("4. Quit")  # Option to exit the program
    choice = input("Enter your choice (1/2/3/4): ")
    return choice


# Function to add a task to the list
def add_task(tasks, task, deadline):
    """
  Adds a task to the list with the specified description and deadline.

  Parameters:
  tasks (list): The current list of tasks.
  task (str): The task description.
  deadline (str): The task deadline.

  Returns:
  list: The updated list of tasks with the new task added.
  """
    tasks.append({'task': task, 'deadline': deadline})  # Add the task and deadline to the list
    print(f"Task '{task}' with deadline {deadline} added to the list.")
    return tasks  # Return the updated tasks list


# Function to view all tasks
def view_tasks(tasks):
    """
  Displays all tasks in the current task list.

  Parameters:
  tasks (list): The current list of tasks.
  """
    if tasks:
        print("\nYour School To-Do List:")
        for idx, task in enumerate(tasks, 1):  # Loop through all tasks and print them
            print(f"{idx}. {task['task']} - Deadline: {task['deadline']}")
    else:
        print("No tasks available")  # Inform the user if no tasks exist


# Function to remove a task by its number
def remove_task(tasks, task_num):
    """
  Removes a task from the list based on its task number.

  Parameters:
  tasks (list): The current list of tasks.
  task_num (int): The task number to remove.

  Returns:
  None
  """
    try:
        # Check if the task number is valid (within the range of tasks)
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)  # Remove the task at the given number
            print(f"Task '{removed_task['task']}' removed from the list.")
        else:
            print("Task number not found.")  # Error message if the task number is invalid
    except ValueError:
        print("Please enter a valid number.")  # Error handling for non-numeric input


# Main function that runs the To-Do List program
def school_todo_list():
    """
  Main loop for the To-Do List program, where the user can add, view, or remove tasks.

  Loops until the user chooses to quit the program.
  """
    tasks = []  # List to store tasks
    while True:
        choice = display_menu()  # Show the menu and get the user's choice

        # If the user chooses to add a task
        if choice == '1':
            task = input("Enter task description: ")
            deadline = input("Enter deadline: ")
            tasks = add_task(tasks, task, deadline)  # Reassign tasks with the updated list

        # If the user wants to view tasks
        elif choice == '2':
            view_tasks(tasks)

        # If the user wants to remove a task
        elif choice == '3':
            try:
                task_num = int(input("Enter task number to remove: "))
                remove_task(tasks, task_num)  # Call the remove_task function
            except ValueError:
                print("Please enter a valid number.")  # Error handling for invalid input

        # If the user chooses to quit
        elif choice == '4':
            print("Goodbye! All tasks have been completed.")  # Exit message
            break
        else:
            print("Invalid choice. Please try again.")  # Error message for invalid menu choice


# Start the program
school_todo_list()
