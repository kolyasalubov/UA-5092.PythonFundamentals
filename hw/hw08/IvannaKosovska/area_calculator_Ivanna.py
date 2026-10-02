from math import pow, pi

def rectangle_area(length, width):
    """
    To calculate the area of rectangle
    """
    return length * width

def triangle_area(base, height):
    """
    To calculate the area of triangle
    """
    return base * height / 2

def circle_area(radius):
    """
    To calculate the area of circle
    """
    return pi * pow(radius, 2)
