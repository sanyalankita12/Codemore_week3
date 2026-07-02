# task1_dictionaries.py

students = {}


def add_student():
    roll = input("Enter Roll Number: ")

    if roll in students:
        print("Student already exists.")
        return

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")

    students[roll] = {
        "Name": name,
        "Age": age,
        "Course": course
    }

    print("Student added successfully.\n")


def search_student():
    roll = input("Enter Roll Number: ")

    if roll in students:
        print(students[roll])
    else:
        print("Student not found.")


def update_student():
    roll = input("Enter Roll Number: ")

    if roll in students:
        students[roll]["Course"] = input("New Course: ")
        print("Updated Successfully.")
    else:
        print("Student not found.")


def display_students():
    if not students:
        print("No records found.")
        return

    for roll, details in students.items():
        print(f"\nRoll: {roll}")
        for key, value in details.items():
            print(f"{key}: {value}")


while True:
    print("\n===== Student Record System =====")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Display Students")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        search_student()

    elif choice == "3":
        update_student()

    elif choice == "4":
        display_students()

    elif choice == "5":
        break

    else:
        print("Invalid choice.")