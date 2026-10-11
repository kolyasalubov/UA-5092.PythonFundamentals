"""
task1
Create a class Ghost

Ghost objects are instantiated without any arguments.

Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" when instantiated
"""

class Ghost(object):
    def __init__(self):
        import random
        c = ["white", "yellow", "purple", "red"]
        self.color = random.choice(c)
   
        
"""
task2
According to the creation myths of the Abrahamic religions, Adam and Eve were the first Humans to wander the Earth.

You have to do God's job. The creation method must return an array of length 2 containing objects (representing Adam and Eve). The first object in the array should be an instance of the class Man. The second should be an instance of the class Woman. Both objects have to be subclasses of Human. Your job is to implement the Human, Man and Woman classes.
"""

def God():
    return [Man(), Woman()]

class Human():
    pass
        
class Man(Human):
    pass

class Woman(Human):
    pass
  

"""
task3
Your task is to complete the Person class. It should have a constructor that accepts a person's name as string and a person's age as integer.

It should also have an info / Info (C#) property/getter/accessor/field (depending on your language) which should evaluate to a formatted string like "johns age is 34", using the person's age and name.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
        
        self.info = f"{name}s age is {age}"
        

"""
task4
"""

import math

class Sphere(object):

    
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
        
    def get_radius(self):
        return self.radius
    
    def get_mass(self):
        return self.mass
    
    def get_volume(self):
        v = (4/3 * math.pi) * (self.radius ** 3)
        v = round(v, 5)
        return v

    def get_surface_area(self):
        s = (4 * math.pi) * (self.radius ** 2)
        s = round(s, 5)
        return s
    
    def get_density(self):
        v = (4/3 * math.pi) * (self.radius ** 3)
        d = self.mass / v
        d = round(d, 5)
        return d
      
      
"""
task5
Proposed function should allow only names with alphanumeric chars (upper & lower letters plus ciphers), but starting only with upper case letter. In other case it should raise an exception.
Disclaimer: there are obviously betters way to check class name than in example cases, but let's stick with that, that Timmy yet has to learn them.
"""

def class_name_changer(cls, new_name):
    nn = list(new_name)
    if new_name[0].isupper() and new_name.isalnum():
        cls.__name__ = new_name
    else:
        raise Exception("Invalid name")
      