# Task 1. Regular Ball Super Ball
class Ball:
    """Represent a ball with a specified type."""
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type


# Task 2. Color Ghost
from random import choice

class Ghost:
    """Create a ghost with a random color."""
    def __init__(self):
        self.color = choice(["white", "yellow", "purple", "red"])


# Task 3. Basic subclasses - Adam and Eve
class Human:
    """Base class for humans."""
    pass

class Man(Human):
    """Represent a man."""
    pass

class Woman(Human):
    """Represent a woman."""
    pass

def God():
    """Create Adam and Eve."""
    return [Man(), Woman()]


# Task 4. Classy Classes
class Person:
    """Represent a person with a name and age."""
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @property
    def info(self):
        return f"{self.name}s age is {self.age}"


# Task 5. Building Spheres
from math import pi

class Sphere:
    """Calculate properties of a sphere."""
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius
    
    def get_mass(self):
        return self.mass
    
    def get_volume(self):
        return round(4 / 3 * pi * self.radius ** 3, 5)
    
    def get_surface_area(self):
        return round(4 * pi * self.radius ** 2, 5)
    
    def get_density(self):
        volume = 4 / 3 * pi * self.radius ** 3
        return round(self.mass / volume, 5)


# Task 6. Python's Dynamic Classes
import re

def class_name_changer(cls, new_name):
    """Change a class name if the new name is valid."""
    if not isinstance(new_name, str) or not re.fullmatch(
        r"[A-Z][a-zA-Z0-9]*", new_name
    ):
        raise ValueError("Invalid class name")
    cls.__name__ = new_name