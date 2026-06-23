
students = []

# Add student
def add_student():
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    

    student = {
        "roll_no": roll_no,
        "name": name,
        "age": age,
        "course": course
        
    }

    students.append(student)
    print("Student added successfully!\n")


# Delete student
def delete_student():
    roll_no = input("Enter Roll Number to delete: ")

    global students
    original_count = len(students)

    students = [s for s in students if s["roll_no"] != roll_no]

    if len(students) < original_count:
        print("Student deleted successfully!\n")
    else:
        print("Student not found!\n")


# Search student
def search_student():
    roll_no = input("Enter Roll Number to search: ")

    result = [s for s in students if s["roll_no"] == roll_no]

    if result:
        print("\nStudent Found:")
        for student in result:
            print(student)
    else:
        print("Student not found!")

    print()


# Display all students
def display_students():
    if not students:
        print("No records available.\n")
        return

    print("\nStudent Records:")
    print("-" * 50)

    for student in students:
        print(
            f"Roll No: {student['roll_no']}, "
            f"Name: {student['name']}, "
            f"Age: {student['age']}, "
            f"Course: {student['course']}"
        )

    print("-" * 50)
    print()


# Main Menu
def main():
    while True:
        print("===== Student Record Manager =====")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Search Student")
        print("4. Display All Students")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            delete_student()
        elif choice == "3":
            search_student()
        elif choice == "4":
            display_students()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.\n")


# Run program
main()
