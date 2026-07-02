# task2_error_handling.py

def divide():
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        result = num1 / num2
        print("Result:", result)

    except ZeroDivisionError:
        print("Cannot divide by zero.")

    except ValueError:
        print("Please enter only numbers.")

    finally:
        print("Program Finished.\n")


def list_access():
    numbers = [10, 20, 30]

    try:
        index = int(input("Enter index: "))
        print(numbers[index])

    except IndexError:
        print("Index out of range.")

    except ValueError:
        print("Invalid input.")


def file_read():
    try:
        file = open("sample.txt", "r")
        print(file.read())
        file.close()

    except FileNotFoundError:
        print("File not found.")


while True:

    print("\n===== Error Handling =====")
    print("1. Divide Numbers")
    print("2. List Access")
    print("3. Read File")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        divide()

    elif choice == "2":
        list_access()

    elif choice == "3":
        file_read()

    elif choice == "4":
        break

    else:
        print("Invalid Choice")