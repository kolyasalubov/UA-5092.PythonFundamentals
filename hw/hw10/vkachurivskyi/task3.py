class Employee:
    """Клас для обліку інформації про працівників компанії"""
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    @classmethod
    def print_total_count(cls):
        """Виводить загальну кількість створених працівників"""
        print(f"Загальна кількість працівників: {cls.total_employees}")

    def display_info(self):
        """Показує інформацію про конкретного працівника"""
        print(f"Ім'я: {self.name}, Зарплата: {self.salary}")

emp_1 = Employee("Олександр", 25000)
emp_2 = Employee("Марія", 30000)

emp_1.display_info()
emp_2.display_info()
Employee.print_total_count()

print(f"Базові класи: {Employee.__bases__}")
print(f"Простір назв: {Employee.__dict__}")
print(f"Назва класу: {Employee.__name__}")
print(f"Назва модуля: {Employee.__module__}")