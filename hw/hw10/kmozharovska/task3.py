MINIMAL_SALARY = 10000


class InvalidSalaryError(ValueError):
    """Raised when an employee's salary is below the minimum."""


class Employee:
    """Represent an employee with a name and salary."""
    counter = 0

    def __init__(self, name: str, salary: float) -> None:
        """Initialize an employee."""
        self.name = name
        self.salary = salary
        Employee.counter += 1

    @property
    def salary(self):
        """Return employee's salary."""
        return self.__salary

    @salary.setter
    def salary(self, amount: float) -> None:
        """Change employee's salary."""
        if amount < MINIMAL_SALARY:
            raise InvalidSalaryError(
                f"Salary shouldn't be less than {MINIMAL_SALARY}.")
        self.__salary = amount

    def display_employee(self) -> None:
        """Display employee's name and salary."""
        print(f"Employee {self.name} earns {self.salary:,.2f} UAH.")

    @classmethod
    def display_count(cls) -> None:
        """Print the total number of employees."""
        print(f"There are {cls.counter} employees.")


# print(Employee.__name__)
# print(Employee.__module__)
# print(Employee.__doc__)
# print(Employee.__base__)
# print(Employee.__dict__)


def main() -> None:
    """Run the Employee class demonstration."""
    Employee.display_count()
    while True:
        try:
            name = input("Enter employee's name: ")
            salary = float(input("Enter employee's salary: "))
            employee1 = Employee(name, salary)
            break
        except InvalidSalaryError as error:
            print(error)
        except ValueError:
            print("Invalid input.")
    employee1.display_employee()
    Employee.display_count()


if __name__ == "__main__":
    main()
