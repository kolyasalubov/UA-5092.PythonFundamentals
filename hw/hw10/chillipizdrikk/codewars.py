"""Solutions to a set of tasks on Python classes from Codewars."""

# 1. Regular Ball Super Ball
# Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.
# If no arguments are given, ball objects should instantiate with a "ball type" of "regular."

class Ball(object):
    """Class that represents a ball with a type."""

    def __init__(self, ball_type: str ="regular") -> None:
        """
        Initialize ball.
 
        Args:
            ball_type: Type of the ball. Defaults to "regular".
        """
        self.ball_type = ball_type


# 2. Color Ghost
# Create a class Ghost. Ghost objects are instantiated without any arguments.
# Ghost objects are given a random color attribute of "white" or "yellow" or 
# "purple" or "red" when instantiated.

import random

color = ["white", "yellow", "purple", "red"]

class Ghost(object):
    """Class that represents a ghost with a random color."""

    def __init__(self):
        """Initialize ghost with a random color from the available colors."""
        self.color = random.choice(color)


# 3. Basic subclasses - Adam and Eve
# According to the creation myths of the Abrahamic religions, Adam and Eve were the 
# first Humans to wander the Earth. You have to do God's job. The creation method must
# return an array of length 2 containing objects (representing Adam and Eve). The first
# object in the array should be an instance of the class Man. The second should be an 
# instance of the class Woman. Both objects have to be subclasses of Human. Your job is 
# to implement the Human, Man and Woman classes.


class Human:
    """Base class that represents a human with a name."""

    def __init__(self, name: str) -> None:
        """
        Initialize human.
 
        Args:
            name: Human's name.
        """
        self.name = name

class Man(Human):
    """Class that represents a man."""

    def __init__(self, name: str) -> None:
        """Initialize man."""
        super().__init__(name)

class Woman(Human):
    """Class that represents a woman."""

    def __init__(self, name: str) -> None:
        """Initialize woman."""
        super().__init__(name)
        
def God() -> list[Human]:
    """Create the first people and return them."""
    return [Man("Adam"), Woman("Eve")]


# 4. Classy Classes
# Your task is to complete the Person class. It should have a constructor that 
# accepts a person's name as string and a person's age as integer.
# It should also have an info / Info (C#) property/getter/accessor/field 
# (depending on your language) which should evaluate to a formatted string like 
# "johns age is 34", using the person's age and name.

class Person:
    """Class that represents a person with a name and an age."""

    def __init__(self, name: str, age: int) -> None:
        """
        Initialize person.
 
        Args:
            name: Person's name.
            age: Person's age.
        """
        self.name = name
        self.age = age
    
    @property
    def info(self) -> str:
        """Get a string with the person's name and age."""
        return f"{self.name}s age is {self.age}"


# 5. Building Spheres
# Arguments for the constructor
# radius -> integer or float (do not round it)
# mass -> integer or float (do not round it)

# Methods to be defined
# get_radius()       =>  radius of the Sphere (do not round it)
# get_mass()         =>  mass of the Sphere (do not round it)
# get_volume()       =>  volume of the Sphere (rounded to 5 place after the decimal)
# get_surface_area() =>  surface area of the Sphere (rounded to 5 place after the decimal)
# get_density()      =>  density of the Sphere (rounded to 5 place after the decimal)

from math import pi

class Sphere(object):
    """Class that represents a sphere with a radius and a mass."""

    def __init__(self, radius: int | float, mass: int | float) -> None:
        """
        Initialize sphere.
 
        Args:
            radius: Sphere's radius.
            mass: Sphere's mass.
        """
        self.radius = radius
        self.mass = mass
        
    def get_radius(self) -> int | float:
        """Return the sphere's radius."""
        return self.radius
    
    def get_mass(self) -> int | float:
        """Return the sphere's mass."""
        return self.mass
    
    def get_volume(self) -> float:
        """Return the sphere's volume."""
        self.volume = round(4/3 * pi * pow(self.radius, 3), 5)
        return self.volume
    
    def get_surface_area(self) -> float:
        """Return the sphere's surface area."""
        self.surface_area = round(4 * pi * pow(self.radius, 2), 5)
        return self.surface_area
    
    def get_density(self) -> float:
        """Return the sphere's density."""
        self.density = round(self.mass / self.volume, 5)
        return self.density


# Python's Dynamic Classes #1
# Timmy's quiet and calm work has been suddenly stopped by his project manager (let's call him boss) yelling:
# - Who named these classes?! Class MyClass? It's ridiculous! I want you to change it to UsefulClass!
# Tim sighed, he already knew it's gonna be a long day. Few hours later, boss came again:
# Much better - he said - but now I want to change that class name to SecondUsefulClass, and went off. Although 
# Timmy had no idea why changing name is so important for his boss, he realized, that it's not the end, so he 
# turned to you, his guru, to help him and asked you to prepare some function, which could change name of given class.

import re

def class_name_changer(cls, new_name: str) -> None:
    """
    Change the name of the given class.
 
    Args:
        cls: Class to rename.
        new_name: New class name. Must start with an uppercase letter
            and contain only letters and digits.
 
    Raises:
        ValueError: If new_name does not match the allowed pattern.
    """
    pattern = r"^[A-Z][A-Za-z0-9]*$"

    if re.fullmatch(pattern, new_name):
        cls.__name__ = new_name
    else:
        raise ValueError