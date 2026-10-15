from __future__ import annotations

import math
import random


# Task 1. Ball-super-ball
# Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.
# If no arguments are given, ball objects should instantiate with a "ball type" of "regular."

class Ball:
    """
    A class representing a ball.
    """

    def __init__(self, ball_type: str = "regular") -> None:
        self.ball_type = ball_type


# Task 2. Color-ghost
# Create a class Ghost.
# Ghost objects are instantiated without any arguments.
# Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" when instantiated


class Ghost:
    """
    A class representing a ghost.
    """

    def __init__(self) -> None:
        self.color = random.choice(["white", "yellow", "purple", "red"])


# Task 3. Basic-subclasses-Adam-and-Eve

# According to the creation myths of the Abrahamic religions, Adam and Eve were the first Humans to wander the Earth.
# You have to do God's job. The creation method must return an array of length 2 containing objects (representing Adam and Eve). 
# The first object in the array should be an instance of the class Man. The second should be an instance of the class Woman. 
# Both objects have to be subclasses of Human. Your job is to implement the Human, Man and Woman classes.

class Human:
    """
    A class representing a human being.
    """
    pass


class Man(Human):
    """
    A class representing a man.
    """
    pass


class Woman(Human):
    """
    A class representing a woman.
    """
    pass


def God() -> list[Human]:
    """
    Creates an array of two objects, one Man and one Woman, both subclasses of Human.
    """
    return [Man(), Woman()]


# Task 4. Classy-classes
# Your task is to complete the Person class. It should have a constructor that accepts a person's name as string 
# and a person's age as integer. It should also have an info / Info (C#) property/getter/accessor/field 
# (depending on your language) which should evaluate to a formatted string like "johns age is 34", 
# using the person's age and name.
# Reference: https://docs.python.org/3/tutorial/classes.html

class Person:
    """
    A class representing a person.
    """

    def __init__(self, name: str, age: int) -> None:
        """
        Initialize a new person with a name and age.
        """

        self.name = name
        self.age = age

    @property
    def info(self) -> str:
        """
        Returns information about the person.
        """

        return f"{self.name}s age is {self.age}"


# Task 5. Building Spheres
# Now that we have a Block let's move on to something slightly more complex: a Sphere.
# 
# Arguments for the constructor: radius, pi, mass, volume, surface area
# radius -> integer or float (do not round it)
# mass -> integer or float (do not round it)
# 
# Methods to be defined
# get_radius()       =>  radius of the Sphere (do not round it)
# get_mass()         =>  mass of the Sphere (do not round it)
# get_volume()       =>  volume of the Sphere (rounded to 5 place after the decimal)
# get_surface_area() =>  surface area of the Sphere (rounded to 5 place after the decimal)
# get_density()      =>  density of the Sphere (rounded to 5 place after the decimal)


class Sphere:
    """
    A class representing a sphere.
    """

    def __init__(self, radius: int | float, mass: int | float) -> None:
        """
        Initialize a new sphere with a radius and mass.
        """

        self.radius = radius
        self.mass = mass

    def get_radius(self) -> int | float:
        """
        Returns the radius of the sphere.
        """

        return self.radius

    def get_mass(self) -> int | float:
        """
        Returns the mass of the sphere.
        """

        return self.mass

    def get_volume(self) -> float:
        """
        Calculates the volume of the sphere.
        """

        volume = (4 / 3) * math.pi * (self.radius ** 3)
        return round(volume, 5)

    def get_surface_area(self) -> float:
        """
        Calculates the surface area of the sphere.
        """

        surface_area = 4 * math.pi * (self.radius ** 2)
        return round(surface_area, 5)

    def get_density(self) -> float:
        """
        Calculates the density (mass / volume), rounded to 5 decimal places.
        """

        volume = (4 / 3) * math.pi * (self.radius ** 3)
        if volume == 0:
            raise ValueError("Radius cannot be zero when calculating density.")
        density = self.mass / volume
        return round(density, 5)


# Task 6. Dynamic Classes

# Note: Proposed function should allow only names with alphanumeric chars (upper & lower letters plus ciphers), 
# but starting only with upper case letter. In other case it should raise an exception.
# Disclaimer: there are obviously betters way to check class name than in example cases, 
# but let's stick with that, that Timmy yet has to learn them.


def class_name_changer(old_name: type, new_name: str) -> None:
    """
    Changes the name of a class.
    """

    if new_name[:1].isupper() and new_name.isalnum():
        old_name.__name__ = new_name
    else:
        raise ValueError(
            f"Invalid class name '{new_name}'."
        )
