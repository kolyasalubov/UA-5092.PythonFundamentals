#Task 1: Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.
#If no arguments are given, ball objects should instantiate with a "ball type" of "regular."

class Ball(object):
    def __init__(self,ball_type = "regular"):
        self.ball_type = ball_type

#Task 2: Create a class Ghost
#Ghost objects are instantiated without any arguments.
#Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" when instantiated
import random
class Ghost(object):
    def __init__(self):
        self.color = random.choice(["white","red","yellow","purple"])


#Task 3: According to the creation myths of the Abrahamic religions, Adam and Eve were the first Humans to wander the Earth.
#You have to do God's job.
# The creation method must return an array of length 2 containing objects (representing Adam and Eve).
# The first object in the array should be an instance of the class Man. The second should be an instance of the class Woman.
# Both objects have to be subclasses of Human. Your job is to implement the Human, Man and Woman classes.


class Human:
    pass
class Man(Human):
    pass
class Woman(Human):
    pass
def God():
    return [Man(), Woman()]


#Task 4: This kata is aimed at teaching basics about classes.
#Task
#Your task is to complete the Person class.
# It should have a constructor that accepts a person's name as string and a person's age as integer.
#It should also have an info / Info (C#) property/getter/accessor/field (depending on your language)
# which should evaluate to a formatted string like "johns age is 34", using the person's age and name.


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def info(self):
        return f"{self.name}s age is {self.age}"


#Task 5: Now that we have a Block let's move on to something slightly more complex: a Sphere.
# Arguments for the constructor
# radius -> integer or float (do not round it)
# mass -> integer or float (do not round it)
# Methods to be defined
# get_radius()       =>  radius of the Sphere (do not round it)
# get_mass()         =>  mass of the Sphere (do not round it)
# get_volume()       =>  volume of the Sphere (rounded to 5 place after the decimal)
# get_surface_area() =>  surface area of the Sphere (rounded to 5 place after the decimal)
# get_density()      =>  density of the Sphere (rounded to 5 place after the decimal)
# Example
# ball = Sphere(2,50)
# ball.get_radius() ->       2
# ball.get_mass() ->         50
# ball.get_volume() ->       33.51032
# ball.get_surface_area() -> 50.26548
# ball.get_density() ->      1.49208
# Any feedback would be much appreciated

from dataclasses import dataclass
import math


@dataclass
class Sphere(object):
    radius: float | int
    mass: float | int
    def get_radius(self):
        return self.radius
    def get_mass(self):
        return self.mass
    def get_volume(self):
        return round(4/3 * math.pi * math.pow(self.radius,3),5)
    def get_surface_area(self):
        return round(4 * math.pi * math.pow(self.radius,2),5)
    def get_density(self):
        return round(self.mass / self.get_volume(),5)


#Task 6: Timmy's quiet and calm work has been suddenly stopped by his project manager (let's call him boss) yelling:
# - Who named these classes?! Class MyClass? It's ridiculous! I want you to change it to UsefulClass!
# Tim sighed, he already knew it's gonna be a long day.
# Few hours later, boss came again:
# Much better - he said - but now I want to change that class name to SecondUsefulClass,
# and went off. Although Timmy had no idea why changing name is so important for his boss, he realized,
# that it's not the end, so he turned to you, his guru, to help him and asked you to prepare some function,
# which could change name of given class.
# Note: Proposed function should allow only names with alphanumeric chars (upper & lower letters plus ciphers),
# but starting only with upper case letter. In other case it should raise an exception.
# Disclaimer: there are obviously betters way to check class name than in example cases, but let's stick with that,
# that Timmy yet has to learn them.


import re
def class_name_changer(cls, new_name):
    pattern = r"^[A-Z][A-Za-z0-9]*$"
    result = re.fullmatch(pattern, new_name)
    if result:
        cls.__name__ = new_name
    else:
        raise ValueError