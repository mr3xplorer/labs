class Employee:
    def __init__(self, emp_id, emp_name, emp_salary, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def input_employee_details(self):
        self.emp_id = input("Enter Employee ID: ")
        self.emp_name = input("Enter Employee Name: ")
        self.emp_salary = float(input("Enter Employee Salary: "))
        self.emp_department = input("Enter Employee Department: ")

    def display_employee_details(self):
        print("\nEmployee Details:")
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee Salary: {self.emp_salary}")
        print(f"Employee Department: {self.emp_department}")

    def update_employee_details(self):
        print("\nUpdate Employee Details:")
        self.emp_name = input(f"Enter updated name for Employee ID {self.emp_id}: ")
        self.emp_salary = float(input(f"Enter updated salary for Employee ID {self.emp_id}: "))
        self.emp_department = input(f"Enter updated department for Employee ID {self.emp_id}: ")

    def calculate_annual_salary(self):
        annual_salary = 12 * self.emp_salary
        print(f"\nAnnual Salary for Employee ID {self.emp_id}: {annual_salary:.2f}")

# Menu-driven system
while True:
    print("\nMenu:")
    print("1. Input Employee Details")
    print("2. Display Employee Details")
    print("3. Update Employee Details")
    print("4. Calculate Annual Salary")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        emp = Employee("", "", 0.0, "")
        emp.input_employee_details()
    elif choice == "2":
        emp.display_employee_details()
    elif choice == "3":
        emp.update_employee_details()
    elif choice == "4":
        emp.calculate_annual_salary()
    elif choice == "5":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
