from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def display_info(self):
        print(f"Name : {self.__name}.")
        print(f"Salary : ${self.__salary}")

    def display_salary(self):
        return self.__salary

    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):    
    def calculate_salary(self):
        return super().display_salary()

class PartTimeEmployee(Employee):    
    def calculate_salary(self):
        sal = super().display_salary() * 0.5
        return sal

fullTime_Emp = FullTimeEmployee("John Doe", 10000)
fullTime_Emp.display_info()

print(fullTime_Emp.calculate_salary())

partTime_Emp = PartTimeEmployee("Jane Doe", 10000)
partTime_Emp.display_info()

print(partTime_Emp.calculate_salary())
