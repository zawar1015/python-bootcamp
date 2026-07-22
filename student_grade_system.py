# Student Grade Management System

students = {}

while True:
    print("\n===== Student Grade Management System =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Display Highest Marks")
    print("4. Display Lowest Marks")
    print("5. Display Average Marks")
    print("6. Search Student")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = float(input("Enter student marks: "))
        students[name] = marks
        print(f"{name} added successfully.")

    elif choice == "2":
        if not students:
            print("No student records found.")
        else:
            print("\nStudent Records:")
            for name, marks in students.items():
                print(f"{name}: {marks}")

    elif choice == "3":
        if not students:
            print("No records available.")
        else:
            highest = max(students.values())
            for name, marks in students.items():
                if marks == highest:
                    print(f"Highest Marks: {name} = {marks}")

    elif choice == "4":
        if not students:
            print("No records available.")
        else:
            lowest = min(students.values())
            for name, marks in students.items():
                if marks == lowest:
                    print(f"Lowest Marks: {name} = {marks}")

    elif choice == "5":
        if not students:
            print("No records available.")
        else:
            average = sum(students.values()) / len(students)
            print(f"Average Marks: {average:.2f}")

    elif choice == "6":
        search = input("Enter student name to search: ")
        if search in students:
            print(f"{search}'s Marks: {students[search]}")
        else:
            print("Student not found.")

    elif choice == "7":
        print("Thank you for using the Student Grade Management System.")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 7.")