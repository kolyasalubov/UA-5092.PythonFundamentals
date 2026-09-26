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


def validate_input_value(message: str) -> float | None:
    """Validate the input value.

    Args:
        message: The message to display

    Returns:
        The input value if it is greater than 0, otherwise None
    """
    try:
        value = float(input(message))
    except ValueError:
        return None

    return value if value > 0 else None


def get_rectangle_area() -> float | None:
    """Read rectangle values and calculate its area.

    Returns:
        The area of the rectangle if the input is valid, otherwise None.
    """
    length = validate_input_value("Enter the length of the rectangle: ")
    width = validate_input_value("Enter the width of the rectangle: ")
    if length is None or width is None:
        return None
    return calculate_area_of_rectangle(length, width)


def get_triangle_area() -> float | None:
    """Read triangle values and calculate its area.

    Returns:
        The area of the triangle if the input is valid, otherwise None.
    """
    base = validate_input_value("Enter the base of the triangle: ")
    height = validate_input_value("Enter the height of the triangle: ")
    if base is None or height is None:
        return None
    return calculate_area_of_triangle(base, height)


def get_circle_area() -> float | None:
    """Read circle values and calculate its area.

    Returns:
        The area of the circle if the input is valid, otherwise None.
    """
    radius = validate_input_value("Enter the radius of the circle: ")
    if radius is None:
        return None
    return calculate_area_of_circle(radius)


def display_result(result: float | None) -> None:
    """Display the result of an area calculation.

    Args:
        result: The result of the area calculation, or None if the input is invalid.
    """
    print(result if result is not None else "ValueError. Try again")


def menu() -> None:
    """Display the menu and handle area calculations until the user exits."""
    while True:
        print("1. Calculate the area of a rectangle")
        print("2. Calculate the area of a triangle")
        print("3. Calculate the area of a circle")
        print("4. Exit")
        choice = input("Enter your choice: ")
        match choice:
            case "1":
                display_result(get_rectangle_area())
            case "2":
                display_result(get_triangle_area())
            case "3":
                display_result(get_circle_area())
            case "4":
                break
            case _:
                print("Invalid command. Please try again.")