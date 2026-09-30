def get_rectangle_values() -> tuple[str, str]:
    """Read rectangle dimensions from user input.

    Returns:
        A tuple containing the length and width of the rectangle as strings.
    """
    length = input("Enter the length of the rectangle: ")
    width = input("Enter the width of the rectangle: ")

    return length, width


def get_triangle_values() -> tuple[str, str]:
    """Read triangle dimensions from user input.

    Returns:
        A tuple containing the base and height of the triangle as strings.
    """
    base = input("Enter the base of the triangle: ")
    height = input("Enter the height of the triangle: ")

    return base, height


def get_circle_value() -> tuple[str]:
    """Read the circle radius from user input.

    Returns:
        A tuple containing the radius of the circle as a string.
    """
    radius = input("Enter the radius of the circle: ")

    return (radius,)