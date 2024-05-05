
# Initialize an empty list to store student details
students = []

# Function to get student details by sno
def get_student_details(sno):
    for student in students:
        if student['Sno'] == sno:
            return student
    return "Student not found."

# Input student details
while True:
    student_info = {}
    student_info["Sno"] = int(input("Enter Sno: "))
    student_info["Name"] = input("Enter student name: ")
    student_info["Roll Number"] = input("Enter roll number: ")
    student_info["Age"] = int(input("Enter age: "))
    student_info["Marks"] = float(input("Enter marks: "))
    students.append(student_info)

    more_students = input("Do you want to input details for more students? (yes/no): ")
    if more_students.lower() != "yes":
        break

# Input the sno of the student to retrieve details
sno_to_search = int(input("Enter the Sno of the student to retrieve details: "))

# Call the function to get student details
result = get_student_details(sno_to_search)

# Display the result
if isinstance(result, dict):
    print("\nStudent Details:")
    for key, value in result.items():
        print(f"{key}: {value}")
else:
    print(result)
