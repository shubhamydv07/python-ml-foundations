def add_student():
    name = input("Enter student name: ").strip()
    while True:
        try:
            marks = int(input("Enter marks out of 100: "))
            if marks < 0 or marks > 100:
                raise ValueError
            break
        except ValueError:
            print("Please enter valid marks (0-100).")

    with open("students.txt", "a") as f:
        f.write(f"{name}:{marks}\n")
    print(f"'{name}' added successfully!")


def display_students():
    try:
        with open("students.txt") as f:
            lines = f.readlines()
        if not lines:
            print("No students found!")
            return
        print("\n--- Student Records ---")
        for i, line in enumerate(lines, start=1):
            name, marks = line.strip().split(":")
            print(f"{i}. {name} → {marks}/100")
    except FileNotFoundError:
        print("No records found!")


def search_student():
    name = input("Enter student name to search: ").strip().lower()
    try:
        with open("students.txt") as f:
            lines = f.readlines()
        for line in lines:
            n, marks = line.strip().split(":")
            if n.lower() == name:
                print(f"Found! {n} → {marks}/100")
                return
        print(f"'{name}' not found!")
    except FileNotFoundError:
        print("No records found!")


while True:
    print("\n1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("0. Exit")

    try:
        choice = int(input("Enter choice: "))
        if choice == 1:
            add_student()
        elif choice == 2:
            display_students()
        elif choice == 3:
            search_student()
        elif choice == 0:
            print("Goodbye!")
            break
        else:
            print("Please enter a valid choice!")
    except ValueError:
        print("Please enter a number!")
    