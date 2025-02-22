class Employee:
    def __init__(self, employee_id, name, position, salary):
        if not isinstance(employee_id, int) or not isinstance(salary, int):
            raise ValueError("Enter only integer values for Employee ID and Salary")
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary
    
    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"
    
class EmployeeManager:
    def __init__(self):
        self.employees = []
        self.load_employees()

    def load_employees(self):
        """Loads employees from the file into the list."""
        try:
            with open("employees.txt", "r") as file_handler:
                for line in file_handler:
                    employee_id, name, position, salary = line.strip().split(", ")
                    self.employees.append(Employee(int(employee_id), name, position, int(salary)))
        except FileNotFoundError:
            pass

    def save_employees(self):
        """Writes all employee records to the file."""
        with open("employees.txt", "w") as file_handler:
            file_handler.write("\n".join(str(emp) for emp in self.employees) + "\n")

    def add_employee(self, emp: Employee):
        self.employees.append(emp)
        self.save_employees()
        print("Employee added successfully!\n")

    def view_all_employees(self):
        if not self.employees:
            print("No employees found\n")
            return
        
        print("Employee list:")
        for emp in self.employees:
            print(emp)
        print("\n")

    def search_employee(self, emp_id):
        """Search for an employee by ID and return the Employee object if found."""
        for emp in self.employees:
            if emp_id == emp.employee_id:
                return emp
        return None

    def update_employee(self, emp_id, new_name=None, new_position=None, new_salary=-1):
        """Updates an employee's details and saves changes to the file."""
        employee = self.search_employee(emp_id)
        if employee is None:
            print("Employee not found\n")
            return 
        
        if new_name:
            if not isinstance(new_name, str):
                raise ValueError("Name must be a string")
            employee.name = new_name 

        if new_position:
            if not isinstance(new_position, str):
                raise ValueError("Position must be a string")
            employee.position = new_position

        if new_salary != -1:
            if not isinstance(new_salary, int):
                raise ValueError("Salary must be an integer")
            employee.salary = new_salary

        self.save_employees()
        print("Employee updated successfully!\n")

    def delete_employee(self, emp_id):
        """Deletes an employee by ID and saves changes to the file."""
        employee = self.search_employee(emp_id)
        if employee:
            self.employees.remove(employee)
            self.save_employees()
            print("Employee deleted successfully!\n")
        else:
            print("Employee not found\n")
    
    def menu(self):
        """Displays the menu options."""
        print("Welcome to the Employee Records Manager!")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit\n")

def main():
    employer = EmployeeManager()
    employer.menu()

    while True:
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 6.\n")
            continue

        if choice == 1:
            try:
                emp_id = int(input("Enter Employee ID: "))
                employee = employer.search_employee(emp_id)
                if employee is None:
                    emp_name = input("Enter Name: ")
                    emp_position = input("Enter Position: ")
                    emp_salary = int(input("Enter Salary: "))
                    emp = Employee(employee_id=emp_id, name=emp_name, position=emp_position, salary=emp_salary)
                    employer.add_employee(emp)
                else:
                    print("Employee exists with this id\n")
            except ValueError:
                print("Invalid input! Employee ID and Salary must be integers.\n")

        elif choice == 2:
            employer.view_all_employees()

        elif choice == 3:
            try:
                employee_id = int(input("Enter Employee ID to search: "))
                employee = employer.search_employee(employee_id)
                if employee:
                    print("Employee found:")
                    print(employee)
                else:
                    print("Employee not found\n")
            except ValueError:
                print("Invalid input! Employee ID must be an integer.\n")

        elif choice == 4:
            try:
                emp_id = int(input("Enter Employee ID to update: "))
                employee = employer.search_employee(emp_id)
                if not employee:
                    print("Employee not found\n")
                    continue

                new_name = input("Enter new name (or press Enter to skip): ").strip()
                new_position = input("Enter new position (or press Enter to skip): ").strip()
                new_salary_input = input("Enter new salary (or press Enter to skip): ").strip()

                new_salary = int(new_salary_input) if new_salary_input else -1
                new_name = new_name if new_name else None
                new_position = new_position if new_position else None

                employer.update_employee(emp_id, new_name, new_position, new_salary)
            except ValueError:
                print("Invalid input! Employee ID and Salary must be integers.\n")

        elif choice == 5:
            try:
                emp_id = int(input("Enter Employee ID: ")) 
                employer.delete_employee(emp_id)
            except ValueError:
                print("Invalid input! Employee ID must be an integer.\n")

        elif choice == 6:
            print("Goodbye!")
            return

        else:
            print("Invalid choice! Please enter a number between 1 and 6.\n")

if __name__ == '__main__':
    main()