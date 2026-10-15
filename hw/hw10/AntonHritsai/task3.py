from dataclasses import dataclass
from pprint import pprint
from typing import ClassVar


@dataclass
class Employee:
    """This is a class representing an employee."""

    name: str
    salary: int
    employee_count: ClassVar[int] = 0

    def __post_init__(self) -> None:
        """Increment the employee count."""
        Employee.employee_count += 1

    @classmethod
    def display_employee_count(cls) -> None:
        """Display the count of employees."""
        print(cls.employee_count)

    def display_employee(self) -> None:
        """Display information about the employee."""
        print(f"Name: {self.name}, salary: {self.salary}")

    def __str__(self) -> str:
        """Return a string representation of the employee."""
        return f"{self.name} - {self.salary}"


if __name__ == "__main__":
    print("Base class:")
    print(Employee.__base__)

    print("\nClass dictionary:")
    pprint(dict(Employee.__dict__))

    print("\nClass name:")
    print(Employee.__name__)

    print("\nModule:")
    print(Employee.__module__)

    print("\nDocumentation:")
    print(Employee.__doc__)