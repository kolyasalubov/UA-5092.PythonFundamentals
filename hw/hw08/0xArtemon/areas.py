from math import pi, pow

def calculate_rectangle_area(side1: float = 1.0, side2: float = 1.0) -> float | None:
    """
    Calculates the area of a rectangle.

    Args:
        side1 (float): The length of the first side. Defaults to 1.0.
        side2 (float): The length of the second side. Defaults to 1.0.

    Returns:
        float | None: The area of the rectangle, or None if sides are invalid.
    """
    if side1 <= 0 or side2 <= 0:
        return None
    return side1 * side2


def calculate_triangle_area(base: float = 1.0, height: float = 2.0) -> float | None:
    """
    Calculates the area of a triangle.

    Args:
        base (float): The base length of the triangle. Defaults to 1.0.
        height (float): The height of the triangle. Defaults to 2.0.

    Returns:
        float | None: The area of the triangle, or None if values are invalid.
    """
    if base <= 0 or height <= 0:
        return None
    return 0.5 * base * height


def calculate_circle_area(radius: float = 1.0) -> float | None:
    """
    Calculates the area of a circle.

    Args:
        radius (float): The radius of the circle. Defaults to 1.0.

    Returns:
        float | None: The area of the circle, or None if radius is invalid.
    """
    if radius <= 0:
        return None
    return pi * pow(radius, 2)