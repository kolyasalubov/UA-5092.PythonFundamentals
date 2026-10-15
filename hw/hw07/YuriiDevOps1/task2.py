import math


def rectangle_area(length, width):
    """
    This function returns the area of a rectangle.
    Args:
        length: The length of the rectangle.
        width: The width of the rectangle.
    Returns:
        The area of the rectangle.
    """
    return length * width


def triangle_area(base, height):
    """
    This function returns the area of a triangle.
    Args:
        base: The length of the triangle base.
        height: The height of the triangle.
    Returns:
        The area of the triangle.
    """
    return 0.5 * base * height


def circle_area(radius):
    """
    This function returns the area of a circle.
    Args:
        radius: The radius of the circle.
    Returns:
        The area of the circle.
    """
    return math.pi * radius ** 2


def read_positive(prompt):
    """
    This function reads a number from the user and checks that it is positive.
    Args:
        prompt: The text shown to the user.
    Returns:
        The entered positive number.
    Raises:
        ValueError: If the input is not a number or is not positive.
    """
    value = float(input(prompt))
    if value <= 0:
        raise ValueError("The value must be positive.")
    return value


choice = input("Choose shape: rectangle, triangle or circle: ").strip().lower()
try:
    if choice == "rectangle":
        length = read_positive("Type length of rectangle: ")
        width = read_positive("Type width of rectangle: ")
        print(round(rectangle_area(length, width), 2))
    elif choice == "triangle":
        base = read_positive("Type length of triangle base: ")
        height = read_positive("Type height of triangle: ")
        print(round(triangle_area(base, height), 2))
    elif choice == "circle":
        radius = read_positive("Type radius of circle: ")
        print(round(circle_area(radius), 2))
    else:
        print("You did not choose the correct shape.")
except ValueError:
    print("Invalid input. Please enter a positive number.")
