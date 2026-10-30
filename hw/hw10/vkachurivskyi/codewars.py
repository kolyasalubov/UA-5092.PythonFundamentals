import random
import math

#1
class Ball:
    def __init__(self, ball_type="regular"):
        """Ініціалізує об'єкт м'яча з певним типом"""
        self.ball_type = ball_type

#2
class Ghost:
    def __init__(self):
        """Надає примарі випадковий колір при створенні"""
        colors = ["white", "yellow", "purple", "red"]
        self.color = random.choice(colors)

#3
class Human:
    def __init__(self):
        """Базовий клас для людини"""
        pass

class Man(Human):
    def __init__(self):
        """Клас Чоловік, що успадковує Людину"""
        super().__init__()

class Woman(Human):
    def __init__(self):
        """Клас Жінка, що успадковує Людину"""
        super().__init__()

class God:
    @staticmethod
    def create():
        """Створює та повертає список з Адамом та Євою"""
        return [Man(), Woman()]


#4
class Person:
    def __init__(self, name, age):
        """Ініціалізує людину з її іменем та віком"""
        self.name = name
        self.age = age
        self.info = f"{name}s age is {age}"


#5
class Sphere:
    def __init__(self, radius, mass):
        """Задає початковий радіус та масу кулі"""
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        """Повертає радіус кулі"""
        return self.radius

    def get_mass(self):
        """Повертає масу кулі"""
        return self.mass

    def get_volume(self):
        """Обчислює та повертає об'єм кулі"""
        volume = (4 / 3) * math.pi * (self.radius ** 3)
        return round(volume, 5)

    def get_surface_area(self):
        """Обчислює та повертає площу поверхні кулі"""
        area = 4 * math.pi * (self.radius ** 2)
        return round(area, 5)

    def get_density(self):
        """Обчислює та повертає щільність кулі"""
        density = self.mass / self.get_volume()
        return round(density, 5)


#6
def create_class(class_name, args):
    """Динамічно створює новий клас із заданим ім'ям та аргументами"""
    def __init__(self, *values):
        for arg, value in zip(args, values):
            setattr(self, arg, value)
            
    return type(class_name, (object,), {"__init__": __init__})