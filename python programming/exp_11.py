def write_student_details(filename):
    with open(filename, 'a') as file:
        name = input("Enter student name: ")
        roll_number = input("Enter roll number: ")
        marks = input("Enter marks: ")
        file.write(f"{name},{roll_number},{marks}\n")
        print("Student details written to the file.")

def read_student_details(filename):
    try:
        with open(filename, 'r') as file:
            print("Student details in the file:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("File not found.")

while True:
    filename = input("Enter the filename: ")
        
    print("\nMenu:")
    print("1. Write student details to a file")
    print("2. Read student details from a file")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        write_student_details(filename)
    elif choice == '2':
        read_student_details(filename)
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")


