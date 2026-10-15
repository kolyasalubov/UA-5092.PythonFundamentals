from collections.abc import Callable

from shapes.validators import validate_input_values
from shapes.get_user_input import (get_rectangle_values,
                                   get_triangle_values,
                                   get_circle_value)
from shapes.calculators import (calculate_area_of_rectangle,
                                calculate_area_of_triangle,
                                calculate_area_of_circle)


def process_calculation(
        get_shape_values: Callable[[], tuple[str, ...]],
        calculate_area_of_shape: Callable[..., float]) -> None:
    """Process user input, validation, calculation, and result output.

    Args:
        get_shape_values: A function that returns the shape values as strings.
        calculate_area_of_shape: A function that calculates the area
            of the shape.
    """
    values = validate_input_values(*get_shape_values())
    if values is not None:
        print(calculate_area_of_shape(*values))
    else:
        print("Invalid input. Please try again.")


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
                process_calculation(
                    get_rectangle_values,
                    calculate_area_of_rectangle
                )
            case "2":
                process_calculation(
                    get_triangle_values,
                    calculate_area_of_triangle
                )
            case "3":
                process_calculation(
                    get_circle_value,
                    calculate_area_of_circle
                )
            case "4":
                break
            case _:
                print("Invalid command. Please try again.")