from math import pi, pow

def rectangle(a: float, b: float) -> float:
    """
    Calculates the area of a rectangle.
    """
    return a * b


def triangle(a: float, h: float) -> float:
    """
    Calculates the area of a triangle.
    """
    return 0.5 * h * a


def circle(r: float) -> float:
    """
    Calculates the area of a circle.
    """
    return pi * pow(r, 2)