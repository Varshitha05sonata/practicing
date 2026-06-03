import json
import logging

# ---------------- LOGGING SETUP ----------------
logging.basicConfig(
    filename="employee_project/application.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

EMP_FILE = "employee_project/employees.json"


# ---------------- LOAD DATA ----------------
def load_employees():
    try:
        with open(EMP_FILE, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        logging.error("employees.json file not found")
        return []

    except json.JSONDecodeError:
        logging.error("Invalid JSON format in employees.json")
        return []


# ---------------- SAVE DATA ----------------
def save_employees(data):
    with open(EMP_FILE, "w") as file:
        json.dump(data, file, indent=4)


# ---------------- ADD EMPLOYEE ----------------
def add_employee():
    try:
        emp_id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        salary = float(input("Enter Salary: "))

        employees = load_employees()

        employees.append({
            "id": emp_id,
            "name": name,
            "salary": salary
        })

        save_employees(employees)

        logging.info(f"Added employee: {name}")

        print("Employee added successfully")

    except ValueError:
        logging.error("Invalid input while adding employee")
        print("Invalid input! Please enter correct values")


# ---------------- VIEW EMPLOYEES ----------------
def view_employees():
    try:
        employees = load_employees()

        if not employees:
            print("No employees found")
            return

        for emp in employees:
            print(emp)

        logging.info("Viewed employee data")

    except Exception as e:
        logging.error(f"Error viewing employees: {e}")
        print("Something went wrong while reading data")


# ---------------- MENU ----------------
while True:
    print("\n===== EMPLOYEE SYSTEM =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        view_employees()

    elif choice == "3":
        logging.info("Application closed")
        print("Goodbye")
        break

    else:
        print("Invalid choice")