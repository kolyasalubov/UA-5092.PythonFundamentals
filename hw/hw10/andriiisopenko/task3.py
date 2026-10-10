class Employee:
    """Represent an employee with a name and salary."""
    total_employees = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1
    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")
    @classmethod
    def display_total(cls):
        print(f"Total employees: {cls.total_employees}")

if __name__ == "__main__":
    employee1 = Employee("John", 3000)
    employee2 = Employee("Anna", 4000)
    employee1.display_info()
    employee2.display_info()
    Employee.display_total()
    print("Base class:", Employee.__base__)
    print("Class namespace:", Employee.__dict__)
    print("Class name:", Employee.__name__)
    print("Module name:", Employee.__module__)
    print("Documentation:", Employee.__doc__)