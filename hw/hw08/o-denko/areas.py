"""
areas.py

Module for calculating the areas of basic geometric figures.
"""

from math import pi


__all__ = [
    "calculate_area_circle",
    "calculate_area_rectangle",
    "calculate_area_triangle",
]


def calculate_area_rectangle(length: int | float, width: int | float) -> int | float:
    """
    Calculate the area of a rectangle.

    length: length of the rectangle
    width: width of the rectangle
    """
    return length * width


def calculate_area_triangle(base: int | float, height: int | float) -> float:
    """
    Calculate the area of a triangle.

    base: base of the triangle
    height: height of the triangle
    """
    return 0.5 * base * height


def calculate_area_circle(radius: int | float) -> float:
    """
    Calculate the area of a circle.

    radius: radius of the circle
    """
    return pi * radius**2
