def calculate_rectangle_area(length: int | float,
                             width: int | float) -> int | float:
    """
    Calculate the area of a rectangle.
    input parameters:
        length - int or float
        width - int or float
    output:
        int or float
    """
    if not (isinstance(length, (int, float))
            and isinstance(width, (int, float))):
        raise TypeError("Both arguments should be int or float data type.")

    if length <= 0 or width <= 0:
        raise ValueError("Both arguments should be positive.")

    return length * width


def calculate_triangle_area(base: int | float, 
                            height: int | float) -> float:
    """
    Calculate the area of a triangle.
    input parameters:
        base - int or float
        height - int or float
    output: float
    """
    if not (isinstance(base, (int, float))
            and isinstance(height, (int, float))):
        raise TypeError("Both arguments should be int or float data type.")

    if base <= 0 or height <= 0:
        raise ValueError("Both arguments should be positive.")

    return (base * height) / 2


def calculate_circle_area(radius: int | float) -> float:
    """
    Calculate the area of a circle.
    input parameters:
        radius - int or float
    output: float
    """
    p = 3.14159

    if not isinstance(radius, (int, float)):
        raise TypeError("Radius should be int or float data type.")

    if radius <= 0:
        raise ValueError("Radius should be positive.")

    return p * radius ** 2


calculate_rectangle_area(10, 5) #50
calculate_triangle_area(8, 5) #20.0
calculate_circle_area(5) #78.53975
