import math


def area_rectangle(width: float , height: float ) -> float:
    """
    Calculate the area of a rectangle.
    Args:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
    Returns:
        float: The area of the rectangle.
    """
    return width * height


def area_triangle(height: float, base: float) -> float:
    """
    Calculate the area of a triangle.
    Args:
        height (float): The height of the triangle (altitude).
        base (float): The length of the triangle's base.
    Returns:
        float: The area of the triangle.
    """
    return 0.5 * height * base


def area_circle(radius: float) -> float:
    """
    Calculate the area of a circle.
    Args:
        radius (float): The radius of the circle.
    Returns:
        float: The area of the circle.
    """
    return math.pi * pow(radius, 2)
