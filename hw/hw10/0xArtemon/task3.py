class Employee:
    """
    A class representing an employee with a name and a salary.
    """

    counter: int = 0

    def __init__(self, name: str, salary: float) -> None:
        """
        Initialize an employee instance.

        :param name: The name of the employee.
        :param salary: The salary of the employee.
        """
        self.name: str = name
        self.salary: float = salary
        Employee.counter += 1

    @classmethod
    def show_stat(cls) -> None:
        """
        Print the total number of employees created.
        """
        print(f"Total number of employees: {cls.counter}")

    def show_info(self) -> None:
        """
        Display detailed information about the employee.
        """
        print(f"The {self.name}'s salary is {self.salary}")

if __name__ == "__main__":
    artem: Employee = Employee("Artem", 2500.0)
    marta: Employee = Employee("Marta", 2600.0)
    
    Employee.show_stat()
    artem.show_info()
    marta.show_info()

    print(f"Base class (__base__): {Employee.__base__}")
    print(f"Class namespace (__dict__): {Employee.__dict__}")
    print(f"Class name (__name__): {Employee.__name__}")
    print(f"Module name (__module__): {Employee.__module__}")
    print(f"Documentation bar (__doc__): {Employee.__doc__}")
