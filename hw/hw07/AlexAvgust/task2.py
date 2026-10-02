import math


def calculate_rectangle_area(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The area of the rectangle.
    """
    return round(length * width, 2)


def calculate_triangle_area(base: float, height: float) -> float:
    """
    Calculate the area of a triangle.

    Args:
        base (float): The base length of the triangle.
        height (float): The height of the triangle.

    Returns:
        float: The area of the triangle.
    """
    return round(0.5 * base * height, 2)


def calculate_circle_area(radius: float) -> float:
    """
    Calculate the area of a circle.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """
    return round(math.pi * radius**2, 2)


def get_shape_area(shape: str, *dimensions) -> float:
    """
    Calculate the area of a given shape.

    Args:
        shape (str): The type of shape ('rectangle', 'triangle', 'circle').
        *dimensions: The dimensions required for the shape.

    Returns:
        float: The area of the shape.
    """
    if shape == "rectangle":
        return calculate_rectangle_area(*dimensions)
    elif shape == "triangle":
        return calculate_triangle_area(*dimensions)
    elif shape == "circle":
        return calculate_circle_area(*dimensions)
    else:
        raise ValueError(
            "Unsupported shape type. Use 'rectangle', 'triangle', or 'circle'."
        )


def input_from_user() -> str:
    """
    Get shape type and dimensions from user input.

    Returns:
        tuple: A tuple containing the shape type and its dimensions.
    """
    shape = input("Enter the shape (rectangle, triangle, circle): ").strip().lower()
    if shape == "rectangle":
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        return f"Area of rectengle: {get_shape_area(shape, length, width)}"
    elif shape == "triangle":
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        return f"Area of triangle: {get_shape_area(shape, base, height)}"
    elif shape == "circle":
        radius = float(input("Enter the radius of the circle: "))
        return f"Area of circle: {get_shape_area(shape, radius)}"
    else:
        raise ValueError(
            "Unsupported shape type. Use 'rectangle', 'triangle', or 'circle'."
        )


print(input_from_user())
