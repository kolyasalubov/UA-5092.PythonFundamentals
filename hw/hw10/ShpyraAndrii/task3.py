class Employee:
    """Employee related functionality"""
    employees_amount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employees_amount += 1

    @classmethod
    def print_employees_amount(cls):
        print(f"Employees amount: {cls.employees_amount}.")

    def print_employee_info(self):
        print(f"Employee name: {self.name}, salary: {self.salary}.")


if __name__ == "__main__":
    john = Employee('John', 20000)
    jane = Employee('Jane', 30000)
    john.print_employee_info()
    jane.print_employee_info()
    Employee.print_employees_amount()

    print(f"Employee.__base__: {Employee.__base__}")
    print(f"Employee.__dict__: {Employee.__dict__}")
    print(f"Employee.__name__: {Employee.__name__}")
    print(f"Employee.__module__: {Employee.__module__}")
    print(f"Employee.__doc__: {Employee.__doc__}")
