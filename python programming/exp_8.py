# Initialize an empty list to store student details
students = []

# Function to input student details
def add_student():
    student_info = {}
    student_info["name"] = input("Enter student name: ")
    student_info["roll_number"] = input("Enter roll number: ")
    students.append(student_info)

# Function to display all student details
def display_students():
    print("\nStudent Details:")
    for student in students:
        print(f"Name: {student['name']}, Roll Number: {student['roll_number']}")

# Function to search for a student by roll number and display details
def search_student(roll_number):
    for student in students:
        if student['roll_number'] == roll_number:
            print(f"Name: {student['name']}, Roll Number: {student['roll_number']}")
            return
    print("Student not found.")

# Menu-driven system
while True:
    print("\nMenu:")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        roll_number = input("Enter roll number to search: ")
        search_student(roll_number)
    elif choice == "4":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
