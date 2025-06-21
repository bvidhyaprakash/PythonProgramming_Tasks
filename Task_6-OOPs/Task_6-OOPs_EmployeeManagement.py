class Employee:
    def __init__(self, name, salary, exp):
        self.name = name
        self.salary = salary
        self.exp = exp

    def calculate_salary(self):
        if self.exp > 5:
            return self.salary + 5000
        return self.salary

class RegularEmployee(Employee):
    def calculate_salary(self):
        base_salary = super().calculate_salary()
        return base_salary + 2000

class ContractEmployee(Employee):
    def calculate_salary(self):
        return super().calculate_salary()

class Manager(Employee):
    def calculate_salary(self):
        base_salary = super().calculate_salary()
        return base_salary + 5000

employee = [
    RegularEmployee("Vidhya", 50000, 3),
    RegularEmployee("B.VP", 50000, 6),
    ContractEmployee("Prakash", 30000, 1),
    Manager("Vidhya Prakash", 80000, 6),
    Manager("Arun Prakash", 80000, 3)
]

print("\nEmployee Salary calculation")
print("---------------------------")
for emp in employee:
    print(f"{emp.name}'s salary is: {emp.calculate_salary()}")