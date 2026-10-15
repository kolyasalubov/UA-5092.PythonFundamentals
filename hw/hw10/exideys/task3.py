from typing import ClassVar


class Employee:
    """Represent an employee with a name and salary."""

    counter: ClassVar[int] = 0

    def __init__(self, name: str, salary: int | float) -> None:
        """
        Initialize a new employee.

        Args:
            name: The employee's name.
            salary: The employee's salary.
        """
        self.name: str = name
        self.salary: int | float = salary
        Employee.counter += 1

    def display_employee(self) -> None:
        """Display information about the employee."""
        print(f"Name: {self.name}, Salary: {self.salary}")

    @classmethod
    def display_count(cls) -> None:
        """Display the total number of employees."""
        print(f"Total employees: {cls.counter}")


if __name__ == "__main__":
    print(Employee.__base__)
    print(Employee.__dict__)
    print(Employee.__name__)
    print(Employee.__module__)
    print(Employee.__doc__)