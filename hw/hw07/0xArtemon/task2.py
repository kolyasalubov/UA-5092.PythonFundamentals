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
    pi = 3.141592653589793
    if radius <= 0:
        return None
    return pi * (radius ** 2)

def print_area_result(shape_name: str, result: float | None) -> None:
    """
    Prints the calculated area or an error message if the result is None.

    Args:
        shape_name (str): The name of the geometric shape.
        result (float | None): The area value or None if inputs were invalid.
    """
    if result is None:
        print("Please enter correct values")
    else:
        print(f"{shape_name} area is {round(result, 2)}")


def make_your_choice() -> None:
    """
    Runs the main interactive menu for area calculations.
    """
    print("Please make your choice:")
    print("1. Calculate rectangle area (enter 1)")
    print("2. Calculate triangle area (enter 2)")
    print("3. Calculate circle area (enter 3)")
    
    choice = int(input("Enter here: "))

    if choice == 1:
        side1 = float(input("Enter first side value: "))
        side2 = float(input("Enter second side value: "))
        result = calculate_rectangle_area(side1, side2)
        print_area_result("Rectangle", result)
            
    elif choice == 2:
        base = float(input("Enter base value: "))
        height = float(input("Enter height value: "))
        result = calculate_triangle_area(base, height)
        print_area_result("Triangle", result)
            
    elif choice == 3:
        radius = float(input("Enter radius value: "))
        result = calculate_circle_area(radius)
        print_area_result("Circle", result)
            
    else:
        print("You entered wrong number! Try again!")

make_your_choice()
