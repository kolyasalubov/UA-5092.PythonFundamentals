from math import pi, pow

def rectangle_area(a, b):
    """Calculate the area of a rectangle."""
    return a * b

def triangle_area(h, a):
    """Calculate the area of a triangle."""
    return 0.5 * h * a

def circle_area(r):
    """Calculate the area of a circle."""
    return pi * pow(r, 2)