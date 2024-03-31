# Task 1:

class Employee:
    def __init__(self, emp_id, emp_name, emp_age, emp_salary, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_age = emp_age
        self.emp_salary = emp_salary
        self.emp_department = emp_department


    def calculate_emp_salary(self, salary, hours_worked):
        if hours_worked > 50:
            overtime = hours_worked - 50
            if self.emp_age >= 40:
                overtime_amount = (overtime * (salary / 50)) * 2
            else:
                overtime_amount = overtime * (salary / 50)
            total_salary = salary + overtime_amount
            return total_salary
        else:
            return salary

    def assign_department(self, new_department):
        self.emp_department = new_department

    def print_employee_details(self):
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.emp_name)
        print("Employee Age:", self.emp_age)
        print("Employee Salary:", self.emp_salary)
        print("Employee Department:", self.emp_department)


emp_id = int(input("Enter Employee ID: "))
emp_name = input("Enter Employee Name: ")
emp_age = int(input("Enter Employee Age: "))
emp_salary = float(input("Enter Employee Salary: "))
emp_department = input("Enter Employee Department: ")

emp = Employee(emp_id, emp_name, emp_age, emp_salary, emp_department)

hours_worked = int(input("Enter number of hours worked by the employee: "))
total_salary = emp.calculate_emp_salary(emp_salary, hours_worked)
print("Total Salary with Overtime:", total_salary)

new_department = input("Enter new department for the employee: ")
emp.assign_department(new_department)

emp.print_employee_details()


# Task 2:

class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance is ${self.balance}")
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance is ${self.balance}")
        else:
            print("Insufficient funds!")
    
    def check_balance(self):
        print(f"Current balance is ${self.balance}")
        

account1 = BankAccount('41794568794', 19300, '25-06-2018', 'Nona Scanfield')
print(account1.account_number)
print(account1.customer_name)
print(account1.date_of_opening)
account1.check_balance()
account1.deposit(500)
account1.withdraw(2000)