class Employee:
    """A class representing an employee."""

    employee_count = 0

    def __init__(self, name: str = "Unknown", salary: float = 0.0) -> None:
        self.name = name
        self.salary = salary
        Employee.employee_count += 1


    def display_count(self) -> None:
           print(Employee.employee_count)


    def display_employee(self) -> None:
         print(f"Name: {self.name}, Salary: {self.salary}")
