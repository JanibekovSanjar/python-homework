def add_employee(employee_id, name, position, salary):
    with open("employees.txt",'a') as f:
        f.write(f"{employee_id}, {name}, {position}, {salary}\n")
    print("*******************************")
    print("Employee added successfully")
    print("*******************************\n")
def display_employees():
    with open("employees.txt") as f:
        info = f.read().strip()
        print("*******************************")
        print(info if info else "No employees found")
        print("*******************************\n")
def search_employee(employee_id):
    with open("employees.txt") as f:
        lines = f.readlines()
        for line in lines:
            info = line.strip().split(", ")
            if info[0] == employee_id:
                print("*******************************")
                print(line)
                print("*******************************\n")
                return
        else:
             print("*******************************")
             print("Employee not found")
             print("*******************************\n")
def employee_update(employee_id, new_name=None, new_position=None, new_salary=None):
    found = False
    with open("employees.txt", "r") as f:
        lines = f.readlines()  
    with open("employees.txt", "w") as f:
        for line in lines:
            info = line.strip().split(", ")  
            if info[0] == employee_id:  
                if new_name is not None:
                    info[1] = new_name
                if new_position is not None:
                    info[2] = new_position
                if new_salary is not None:
                    info[3] = str(new_salary) 
                found = True  
            f.write(", ".join(info) + "\n") 
    if found:
        print("*******************************")
        print("Employee information updated successfully")
        print("*******************************\n")
    else:
        print("*******************************")
        print("Employee not found") 
        print("*******************************\n")
def delete_employee(employee_id):
    found = False
    with open("employees.txt", "r") as f:
        lines = f.readlines()  
    with open("employees.txt", "w") as f:
        for line in lines:
            info = line.strip().split(", ")  
            if info[0] == employee_id:  
                found = True  
                continue
            f.write(line) 
    if found:
        print("*******************************")
        print("Employee information deleted successfully")
        print("*******************************\n")
    else:
        print("*******************************")
        print("Employee not found") 
        print("*******************************\n")
while True:
    print("1. Add new employee record")
    print("2. View all employee records")
    print("3. Search for an employee by Employee ID")
    print("4. Update an employee's information")
    print("5. Delete an employee record")
    print("6. Exit")
    
    choice = input("Enter your choice: \n>>>")

    if choice == "1":
        emp_id = input("Enter employee ID:\n>>>")
        employee_name = input("Enter employee name:\n>>>")
        employee_position = input("Enter the position of employee:\n>>>")
        employee_salary = input("Enter the salary of employee:\n>>>")
        add_employee(emp_id, employee_name, employee_position,employee_salary)
    elif choice == "2":
        display_employees()
    elif choice == "3":
        emp_id = input("Enter employee ID:\n>>>")
        search_employee(emp_id)
    elif choice == "4":
        emp_id = input("Enter Employee ID to update: \n>>>")
        new_name = input("Enter new name (or press Enter to skip): \n>>>")
        new_position = input("Enter new position (or press Enter to skip): \n>>>")
        new_salary = input("Enter new salary (or press Enter to skip): \n>>>")
        new_name = new_name if new_name.strip() else None
        new_position = new_position if new_position.strip() else None
        new_salary = new_salary if new_salary.strip() else None

        employee_update(emp_id, new_name, new_position, new_salary)

    elif choice == "5":
        with open("employees.txt","r") as f:
            content = f.read()
        if content.strip():
            emp_id = input("Enter employee ID:\n>>>")
            delete_employee(emp_id)
        else:
            print("*******************************")
            print("No employees found")
            print("*******************************\n")
    elif choice == "6":
        break
    else:
        print("*******************************")
        print("Invalid choice, please try again.")
        print("*******************************\n")