from __future__ import annotations
from pprint import pprint


class Employee:
    """
    A class representing an employee.
    """

    count: int = 0

    def __init__(self, name: str, salary: int | float) -> None:
        """
        Initialize a new employee with a name and salary.
        """
        if not name or not name.strip():
            raise ValueError("Name cannot be empty.")
        if salary < 0:
            raise ValueError("Salary cannot be negative.")

        self.name = name.strip()
        self.salary = salary
        Employee.count += 1

    @classmethod
    def total_employees(cls) -> None:
        """
        Print the total number of employees.
        """
        print(f"Total number of employees: {cls.count}")

    def display_employee_info(self) -> None:
        """
        Display information about each employee in particular, 
        namely the name and salary.
        """
        print(f"Name: {self.name}, Salary: {self.salary}")

    def __del__(self) -> None:
        """
        Decrement the employee count when an employee instance is destroyed.
        """
        if hasattr(self, 'name'):
            Employee.count -= 1


if __name__ == '__main__':
    emp1 = Employee("Alice", 50000)
    emp2 = Employee("Bob", 65000)

    emp1.display_employee_info()
    emp2.display_employee_info()

    Employee.total_employees()

    print("\nDeleting emp1 ('Alice')...")
    del emp1
    Employee.total_employees()

    print("\n" + "=" * 50 + "\n")
    print("Employee metadata:\n")
    print("  Base class (__base__):", Employee.__base__)
    print("  Class name (__name__):", Employee.__name__)
    print("  Module name (__module__):", Employee.__module__)
    print("  Documentation string (__doc__):", Employee.__doc__)
    print("  Class namespace (__dict__):\n")
    pprint(dict(Employee.__dict__), indent=4)
