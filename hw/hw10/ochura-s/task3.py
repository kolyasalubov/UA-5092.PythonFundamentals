class Employee:
    """
    An employee with a name and salary. Keeps count of all employees.
    """

    __count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.__count += 1

    @classmethod
    def display_count(cls):
        print(f"Total employees: {cls.__count}")

    def display_employee(self):
        print(f"Name: {self.name}, Salary: {self.salary}")


employees = [Employee("Anna", 2000), Employee("Bohdan", 3500), Employee("Olena", 4200)]
for employee in employees:
    employee.display_employee()
Employee.display_count()

print("Employee.__base__:", Employee.__base__)
print("Employee.__dict__:", Employee.__dict__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__doc__:", Employee.__doc__)
