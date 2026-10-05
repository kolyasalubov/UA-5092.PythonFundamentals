from random import choice
from math import pi
import re


class Ball(object):
    """Create a class Ball.
    Ball objects should accept one argument for "ball type" when instantiated.
    If no arguments are given, ball objects should instantiate
    with a "ball type" of "regular."
    """
    def __init__(self, ball_type='regular'):
        self.ball_type = ball_type


class Ghost(object):
    """Ghost objects are instantiated without any arguments.
    Ghost objects are given a random color attribute of
    "white" or "yellow" or "purple" or "red" when instantiated
    """
    random_colors = ['white', 'yellow', 'red', 'purple']

    def __init__(self):
        self.color = choice(Ghost.random_colors)


"""The creation method must return an array of length 2 containing objects
(representing Adam and Eve). The first object in the array
should be an instance of the class Man.
The second should be an instance of the class Woman.
Both objects have to be subclasses of Human.
"""


class Human():
    pass


class Man(Human):
    pass


class Woman(Human):
    pass


def God():
    return [Man(), Woman()]


class Person:
    """To complete the Person class.
    It should have a constructor that accepts a person's name
    as string and a person's age as integer. It should also have an info
    property/getter/accessor/field (depending on your language) which should
    evaluate to a formatted string like "johns age is 34",
    using the person's age and name."""
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def info(self):
        """Gets the person's main info."""
        return f"{self.__name}s age is {self.__age}"


class Sphere(object):
    """Sphere objects are instantiated with a radius and a mass.
    They provide getters for the radius and mass, and methods
    to calculate the sphere's volume, surface area and density.
    """
    def __init__(self, radius, mass):
        self.__radius = radius
        self.__mass = mass
        
    def get_radius(self):
        return self.__radius
    
    def get_mass(self):
        return self.__mass
    
    def get_volume(self):
        return (4 / 3) * pi * self.__radius ** 3
    
    def get_volume(self):
        return (4 / 3) * pi * self.__radius ** 3
    
    def get_density(self):
        return self.__mass / self.get_volume()
    
    def get_surface_area(self):
        return 4 * pi * self.__radius ** 2


def class_name_changer(cls, new_name):
    """Change the name of the given class to new_name.
    The new name must start with an uppercase letter followed by
    word characters, otherwise ValueError is raised.
    """
    class_name_pattern = r"^[A-Z]+\w+$"
    if not re.match(class_name_pattern, new_name):
        raise ValueError()
    cls.__name__ = new_name