from math import pi, pow


def rectangle(a: float, b: float) -> float | bool: 
    """
    Calculates the area of a rectangle.

    Args:
        a - the length of the rectangle.
        b - the width of the rectangle.

    Returns:
        The area of the rectangle.
    """

    if a <= 0 or b <= 0:
        return False
    
    return a * b


def triangle(a: float, h: float) -> float | bool:
    """
    Calculates the area of a triangle.

    Args:
        a - the base of the triangle.
        h - the height of the triangle.

    Returns:
        The area of the triangle.
    """
    if a <= 0 or h <= 0:
        return False
    
    return 0.5 * h * a


def circle(r: float) -> float | bool:
    """
    Calculates the area of a circle.

    Args:
        r - the radius of the circle.

    Returns:
        The area of the circle.
    """

    if r <= 0:
        return False
    
    return pi * pow(r, 2)