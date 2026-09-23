from math import pi, pow

"""
The module provides functions to calculate the area of a figure.
(rectangle, triangle, circle)
"""

figure = ""


def calculate_rectangle_area(length: float,
                             width: float) -> float:
    """
    Calculate the area of a rectangle.
    Args:
        length - float
        width - float
    Returns: float
    """
    if length <= 0 or width <= 0:
        raise ValueError("Both arguments should be positive.")

    return length * width


def calculate_triangle_area(base: float,
                            height: float) -> float:
    """
    Calculate the area of a triangle.
    Args:
        base - float
        height - float
    Returns: float
    """
    if base <= 0 or height <= 0:
        raise ValueError("Both arguments should be positive.")

    return 0.5 * height * base


def calculate_circle_area(radius: float) -> float:
    """
    Calculate the area of a circle.
    Args: radius - float
    Returns: float
    """
    if radius <= 0:
        raise ValueError("Radius should be positive.")

    return pi * pow(radius, 2)
