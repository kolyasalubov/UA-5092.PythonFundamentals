from math import pi, pow

def rectangle_area(a: float, b: float) -> float:
    """
    Return the area of a rectangle with sides a and b
    """
    return a * b


def triangle_area(base: float, height: float) -> float:
    """
    Return the area of a triangle with the given base and height
    """
    return 0.5 * base * height


def circle_area(radius: float) -> float:
    """
    Return the area of a circle with the given radius
    """
    return pi * pow(radius, 2)