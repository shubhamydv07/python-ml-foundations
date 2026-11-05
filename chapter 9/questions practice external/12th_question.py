def add_task():
    task = input("Enter task: ").strip()
    with open("tasks.txt", "a") as f:
        f.write(task + "\n")
    print(f"'{task}' added successfully!")

def view_task():
    try:
        with open("tasks.txt") as f:
            lines = f.readlines()
        if not lines:
            print("No tasks found!")
            return
        print("\n--- Tasks ---")
        for i, line in enumerate(lines, start=1):
            print(f"{i}. {line.strip()}")
    except FileNotFoundError:
        print("No tasks found!")

def delete_task():
    try:
        with open("tasks.txt") as f:
            lines = f.readlines()
        if not lines:
            print("No tasks found!")
            return
        print("\n--- Tasks ---")
        for i, line in enumerate(lines, start=1):   
            print(f"{i}. {line.strip()}")
        task_number = int(input("Enter task number to delete: "))
        if task_number < 1 or task_number > len(lines):
            print("Invalid task number!")
            return
        removed = lines.pop(task_number - 1)
        with open("tasks.txt", "w") as f:
            f.writelines(lines)
        print(f"'{removed.strip()}' deleted successfully!")
    except FileNotFoundError:
        print("No tasks found!")
    except ValueError:
        print("Please enter a valid number!")

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("0. Exit")

    choice = input("Enter choice: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_task()
    elif choice == "3":
        delete_task()
    elif choice == "0":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")