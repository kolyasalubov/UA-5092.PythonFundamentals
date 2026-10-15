# 1. Regular Ball Super Ball
class Ball(object):
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type

# 2. Color Ghost
import random

class Ghost(object):
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])

# 3. Basic subclasses - Adam and Eve
class Human():
    pass
    
class Man(Human):
    pass
    
class Woman(Human):
    pass
    
def God():
    Adam = Man()
    Eve = Woman()
    return [Adam, Eve]

# 4. Classy Classes
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        
    def __get_info(self):
        return f"{self.name}s age is {self.age}"
    
    info = property(__get_info)

# 5. Building Spheres
import math

class Sphere(object):
    def __init__(self, radius: float, mass: float):
        self.radius = radius
        self.mass = mass
        self.volume = 4 / 3 * math.pi * radius ** 3
        self.area = 4 * math.pi * radius ** 2
        
    def get_radius(self):
        return self.radius
        
    def get_mass(self):
        return self.mass
    
    def get_volume(self):
        return round(self.volume, 5)
    
    def get_surface_area(self):
        return round(self.area, 5)
    
    def get_density(self):
        return round(self.mass / self.volume, 5)

# 6. Python's Dynamic Classes #1
import re

def class_name_changer(cls, new_name):
    if re.match("^[A-Z][a-zA-Z0-9]*$", new_name):
        cls.__name__ = new_name
    else:
        raise Exception("Wrong class name!")
