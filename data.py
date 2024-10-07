import csv
import random
from datetime import datetime, timedelta

def generate_employee_id():
    return f"EMP{random.randint(10000, 99999)}"

def generate_name():
    first_names = ["John", "Jane", "Michael", "Emily", "David", "Sarah", "Robert", "Lisa"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def generate_date_of_birth():
    start_date = datetime(1960, 1, 1)
    end_date = datetime(2000, 12, 31)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    return start_date + timedelta(days=random_number_of_days)

def generate_department():
    departments = ["HR", "IT", "Finance", "Marketing", "Sales", "Operations"]
    return random.choice(departments)

def generate_salary():
    return round(random.uniform(30000, 150000), 2)

def generate_ssn():
    return f"{random.randint(100, 999)}-{random.randint(10, 99)}-{random.randint(1000, 9999)}"

def generate_employee_data(num_employees):
    employees = []
    for _ in range(num_employees):
        employee = {
            "EmployeeID": generate_employee_id(),
            "Name": generate_name(),
            "DoB": generate_date_of_birth().strftime("%Y-%m-%d"),
            "Department": generate_department(),
            "Salary": generate_salary(),
            "SSN": generate_ssn()
        }
        employees.append(employee)
    return employees

def write_to_csv(employees, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ["EmployeeID", "Name", "DoB", "Department", "Salary", "SSN"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for employee in employees:
            writer.writerow(employee)

if __name__ == "__main__":
    num_employees = 1000
    filename = "employees.csv"
    employees = generate_employee_data(num_employees)
    write_to_csv(employees, filename)
    print(f"Generated {num_employees} employee records and saved to {filename}")