"""Module for working with employees."""

class Employee:
    """Class for employees with a name, a salary and a shared counter."""

    __counter: int = 0

    def __init__(self, name: str, salary: float) -> None:
        """
        Initialize employee.

        Args:
            name: Employee's name.
            salary: Employee's salary.
        """
        self.name = name
        self.__salary = salary
        Employee.__counter += 1

    @classmethod
    def print_count(cls) -> None:
        """Print the total number of employees."""
        print(f"Total number of employees: {cls.__counter}")

    @property
    def salary(self) -> float:
        """Get employee's salary."""
        return self.__salary

    def display_info(self) -> None:
        """Print employee's name and salary."""
        print(f"{self.name}'s salary is {self.__salary}")


def main() -> None:
    """Display each employee's info and class info."""
    emp1 = Employee("Kate", 20500)
    emp2 = Employee("Jake", 31000)

    for emp in (emp1, emp2):
        emp.display_info()
    print()

    Employee.print_count()

    print("-" * 50)
    print("Class info:\n")
    print("__base__:  ", Employee.__base__, "\n")
    print("__dict__:  ", Employee.__dict__, "\n")
    print("__name__:  ", Employee.__name__, "\n")
    print("__module__:", Employee.__module__, "\n")
    print("__doc__:   ", Employee.__doc__, "\n")


if __name__ == "__main__":
    main()