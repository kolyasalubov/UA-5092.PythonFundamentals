class Employee:
    """Модель для обліку та управління даними персоналу компанії."""

    total_staff: int = 0

    def __init__(self, full_name: str, monthly_salary: float) -> None:
        """Реєструє нового співробітника та оновлює лічильник штату."""
        self.full_name = full_name
        self.monthly_salary = monthly_salary
        Employee.total_staff += 1

    @classmethod
    def show_total_staff(cls) -> None:
        """Виводить актуальну кількість співробітників у компанії."""
        print(f"Total number of employees: {cls.total_staff}")

    def show_card(self) -> None:
        """Демонструє картку співробітника із форматованою зарплатою."""
        print(f"Employee Name: {self.full_name}, Salary: {self.monthly_salary:,.2f}")


if __name__ == "__main__":
    worker_1 = Employee("Alex", 20000)
    worker_2 = Employee("Naya", 30000)

    worker_1.show_card()
    worker_2.show_card()
    Employee.show_total_staff()

    print("\n--- Employee Class System Information ---")
    print(f"Base classes (__base__): {Employee.__base__}")
    print(f"Class namespace (__dict__): {Employee.__dict__}")
    print(f"Class name (__name__): {Employee.__name__}")
    print(f"Module name (__module__): {Employee.__module__}")
    print(f"Documentation bar (__doc__): {Employee.__doc__}")


