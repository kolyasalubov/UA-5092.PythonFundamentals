import random 
import math
import re


# I. Ball-super-ball

class Ball:
    """Клас для створення м'яча з певним типом."""

    def __init__(self, ball_type: str = "regular"):
        """Ініціалізує м'яч. За замовчуванням тип 'regular'."""
        self.ball_type = ball_type



# II. Color-ghost

class Ghost:
    """Клас для створення привидів випадкового кольору."""

    def __init__(self):
        """Ініціалізує привида та присвоює йому випадковий колір."""
        colors = ["white", "yellow", "purple", "red"]
        self.color = random.choice(colors)



# III. Basic-subclasses-Adam-and-Eve

class Human:
    """Базовий клас для людини."""
    def __init__(self, name):
        self.name = name

class Man(Human):
    """Клас для чоловіка (Адама)."""
    def __init__(self):
        super().__init__("Adam")

class Woman(Human):
    """Клас для жінки (Єви)."""
    def __init__(self):
        super().__init__("Eve") 

def God():
    """Створює та повертає список з Адама та Єви."""
    return [Man(), Woman()]



# IV. Classy-classes

class Person:
    """Клас, що описує людина з іменем та віком."""

    def __init__(self, name: str, age: int):
        """Ініціалізує людину."""
        self.name = name
        self.age = age

    @property
    def info(self) -> str:
        """Повертає форматований рядок з інформацією про людину."""
        return f"{self.name}s age is {self.age}"



# V. Building Spheres

class Sphere:
    """Клас для роботи з геометричною кулею."""

    def __init__(self, radius: float, mass: float):
        """Ініціалізує кулю радіусом та масою."""
        self.radius = radius
        self.mass = mass

    def get_radius(self) -> float:
        """Повертає радіус кулі."""
        return self.radius

    def get_mass(self) -> float:
        """Повертає масу кулі."""
        return self.mass

    def get_volume(self) -> float:
        """Повертає об'єм кулі, округлений до 5 знаків."""
        v = (4 / 3) * math.pi * (self.radius ** 3)
        return round(v, 5)

    def get_surface_area(self) -> float:
        """Повертає площу поверхні кулі, округлену до 5 знаків."""
        a = 4 * math.pi * (self.radius ** 2)
        return round(a, 5)

    def get_density(self) -> float:
        """Повертає густину кулі, округлену до 5 знаків."""
        v = (4 / 3) * math.pi * (self.radius ** 3)
        return round(self.mass / v, 5)



# VI. Dynamic Classes

def class_name_changer(cls, new_name: str) -> None:
    """Динамічно змінює ім'я заданого класу.

    new_name -- нове ім'я (повинно починатися з великої літери та містити лише букви/цифри)
    """
    if not re.match(r"^[A-Z][A-Za-z0-9]*$", new_name):
        raise ValueError("Invalid class name")
        
    cls.__name__ = new_name
