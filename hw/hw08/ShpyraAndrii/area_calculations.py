from math import pi, pow


def get_rectangle_area(height, width):
    """Calculates the area of a rectangle"""
    return height * width


def get_triangle_area(height, base):
    """Calculates the area of a triangle"""
    return height * base * 0.5


def get_circle_area(radius):
    """Calculates the area of a circle"""
    return pow(radius, 2) * pi
