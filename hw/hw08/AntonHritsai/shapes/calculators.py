from math import pi, pow


def calculate_area_of_rectangle(l: float | int, w: float | int) -> float:
    """Calculate the area of a rectangle given its length and width.

    Args:
        l: The length of the rectangle
        w: The width of the rectangle

    Returns:
        The area of the rectangle
    """
    return l * w


def calculate_area_of_triangle(b: int | float, h: int | float) -> float:
    """Calculate the area of a triangle given its base and height.

    Args:
        b: The base of the triangle
        h: The height of the triangle

    Returns:
        The area of the triangle
    """
    return b * h / 2


def calculate_area_of_circle(r: float | int) -> float:
    """Calculate the area of a circle given its radius.

    Args:
        r: The radius of the circle

    Returns:
        The area of the circle
    """
    return pi * pow(r, 2)