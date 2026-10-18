class Employee:
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    def display_info(self):
        print(f"Name: {self.name}, salary: {self.salary}")

    @classmethod
    def get_total_employees(cls):
        print(f"Total employees: {cls.total_employees}")

emp1 = Employee("Maxym", 500000)
emp2 = Employee("Sasha", 600000)

emp1.display_info()
emp2.display_info()
Employee.get_total_employees()

print("\nInformation about the Employee class:")
print(f"Basic class (__base__): {Employee.__base__}")
print(f"Namespace (__dict__): {Employee.__dict__}")
print(f"Class name (__name__): {Employee.__name__}")
print(f"Module (__module__): {Employee.__module__}")
print(f"Documentation (__doc__): {Employee.__doc__}")