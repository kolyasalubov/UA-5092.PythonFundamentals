from math import pi, pow


def rectangle_area(a: float, b: float) -> float:
    """Return the area of a rectangle with sides `a` and `b`: S = a * b."""
    return a * b


def triangle_area(a: float, h: float) -> float:
    """Return the area of a triangle with base `a` and height `h`: S = 0.5 * h * a."""
    return 0.5 * h * a


def circle_area(r: float) -> float:
    """Return the area of a circle with radius `r`: S = pi * r ** 2."""
    return pi * pow(r, 2)
