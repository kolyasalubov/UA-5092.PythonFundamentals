class Employee:
    number_of_employees = 0
    """
    Base class for all employees. Stores name, salary, and total employee count.
    """
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
        Employee.number_of_employees += 1
        
    def Number_of_employees(self):
        return self.number_of_employees
    
    def Employee_information(self):
        return f"Employee name: {self.name}, salary: {self.salary}."



emp1 = Employee("Alex", 1000)
emp2 = Employee("Gleb", 2500)


print(emp1.Employee_information())
print(emp2.Employee_information())

print(emp1.Number_of_employees())

print("--------------------------------")

print("Base class:", Employee.__base__)
print("Namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module:", Employee.__module__)
print("Documentation:", Employee.__doc__)