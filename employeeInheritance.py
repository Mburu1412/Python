"""
Inheritance in Python
"""
from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, emp_ID, name, salary):
        self.emp_ID = emp_ID
        self.name = name
        self.salary = salary
        
    @abstractmethod
    def calculate_Salary(self): #Forces all classes to implement the function if the class is inherited
        pass

class HourlyEmployee(Employee):
    def __init__(self,emp_ID, name, salary, hourly_rate, hours_worked):
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        Employee.__init__(self, emp_ID, name, salary)

    def calculate_Salary(self):
        self.salary = self.hourly_rate * self.hours_worked
        return self.salary

class SalariedEmployee(Employee):
    def __init__(self, emp_ID, name, salary, monthly_salary):
        self.monthly_salary = monthly_salary
        Employee.__init__(self, emp_ID, name, salary)

    def calculate_Salary(self):
        self.salary = self.monthly_salary
        return self.salary

#Object Creation
hourly_Emp = HourlyEmployee(101, "Alice", 0, 20, 160)
print(f"Alice's initial salary  : ${hourly_Emp.salary}")

hourly_Emp.calculate_Salary()
print(f"Alice Calculated Salary : ${hourly_Emp.salary}")

salaried_Emp = SalariedEmployee(102, "Bob", 0, 20000)
print(f"Bob's initial salary : ${salaried_Emp.salary}")

salaried_Emp.calculate_Salary()
print(f"Bob Calculated Salary : ${salaried_Emp.salary}")
