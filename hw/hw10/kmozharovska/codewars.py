import random
import re
from math import pi

# I. Ball-super-ball


class Ball:
    """Represent a ball with a ball type."""
    def __init__(self, ball_type: str = "regular") -> None:
        """Initialize a ball with a ball type."""
        self.ball_type = ball_type


# II. Color-ghost

COLORS_SET = {"white", "yellow", "purple", "red"}


class Ghost:
    """Represent a ghost."""
    def __init__(self) -> None:
        """Initialize a ghost with a random color."""
        self.color = random.choice(list(COLORS_SET))


# III. Basic-subclasses-Adam-and-Eve

class Human:
    """Represent a human."""
    def __init__(self, name: str) -> None:
        """Initialize a human with name."""
        self.name = name


class Man(Human):
    """Represent a man."""
    def __init__(self, name: str) -> None:
        """Initialize a man with name."""
        super().__init__(name)
        self.sex = "male"


class Woman(Human):
    """Represent a woman."""
    def __init__(self, name: str) -> None:
        """Initialize a woman with name."""
        super().__init__(name)
        self.sex = "female"


def God() -> list:
    """Return the list of the first humans."""
    return [Man("Adam"), Woman("Eve")]


# IV. Classy-classes

class Person:
    """Represent a person."""
    def __init__(self, name: str, age: int) -> None:
        """Initialize a person with name and age."""
        self.name = name
        self.age = age

    @property
    def info(self) -> str:
        """Return person's info."""
        return f"{self.name}s age is {self.age}"


# V. Building Spheres

class Sphere:
    """Represent a sphere."""
    def __init__(self, radius: int | float, mass: int | float) -> None:
        """Initialize a sphere with radius and mass."""
        self.radius = radius
        self.mass = mass

    def get_radius(self) -> int | float:
        """Return sphere's radius."""
        return self.radius

    def get_mass(self) -> int | float:
        """Return sphere's mass."""
        return self.mass

    def get_volume(self) -> float:
        """Calculate sphere's volume."""
        return round(4 / 3 * pi * self.radius ** 3, 5)

    def get_surface_area(self) -> float:
        """Calculate sphere's area."""
        return round(4 * pi * self.radius ** 2, 5)

    def get_density(self) -> float:
        """Calculate sphere's density."""
        return round(self.mass / self.get_volume(), 5)


# VI. Dynamic Classes

NAME_PATTERN = r"^[A-Z][A-Za-z0-9]*$"


def class_name_changer(cls, new_name: str) -> None:
    """Change class name."""
    if not re.fullmatch(NAME_PATTERN, new_name):
        raise ValueError("Invalid class name")

    cls.__name__ = new_name
