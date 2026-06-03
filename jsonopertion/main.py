import json

with open("jsonopertion/employees.json", "r") as file:
    employees = json.load(file)

for emp in employees:
    print(f"Name: {emp['name']}")
    print(f"Salary: {emp['salary']}")
    print("-" * 20)