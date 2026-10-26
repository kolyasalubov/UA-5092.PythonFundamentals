import math
from tools.errors import LessThenZeroError, TriangleSidesError
from tools.inputnumber import input_number, input_figure_parameter

def calculate_rectangle_area(side1: int|float, side2: int|float) -> int|float:
    """
    Function calculates area of the rectangle
    Args:
        side1 (int|float): Length of one side of rectangle
        side2 (int|float): Length of another side of rectangle
    Returns:
        int|float: Calculated rectangle area
    """

    return round(side1 * side2, 2)

def calculate_triangle_area(side1: int|float, side2: int|float, side3: int|float) -> int|float:
    """
    Function calculates area of the triangle by Heron's formula
    Args:
        side1 (int|float): Length of one side of triangle
        side2 (int|float): Length of another side of triangle
        side3 (int|float): Length of third side of triangle      
    Returns:
        int|float: Calculated triangle area
    """
    s = (side1 + side2 + side3) / 2
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    return round(area, 2)

def calculate_circle_area(radius: int|float) -> int|float:
    """
    Function calculates area of the circle
    Args:
        radius (int|float): radius of the circle
    Returns:
        int|float: Calculated circle area
    """
    return round(math.pi * (radius ** 2), 2)

def validate_triangle_sides(side_1: int|float, side_2: int|float, side_3: int|float):
    """
    Function to validate triangle sides, so one side always should be less than sum of other two sides
    Args:
        side_1 (int|float): first edge of triangle
        side_2 (int|float): second edge of triangle
        side_3 (int|float): third edge of triangle
    Raises:
        TriangleSidesError: Custom error type, raised when one of the edges longer then sum of two other
    """
    err_message = ""
    if side_1 >= side_2 + side_3:
        err_message = f"{side_1} >= {side_2} + {side_3}"
    elif side_2 >= side_1 + side_3:
        err_message = f"{side_2} >= {side_1} + {side_3}"
    elif side_3 >= side_1 + side_2:
        err_message = f"{side_3} >= {side_1} + {side_2}"

    if err_message:
        raise TriangleSidesError(f"Invalid triangle: cannot be {err_message}")

def action_if_rectangle() -> float:
    """
    Function to perform action if user have chosen rectangle, prints area of rectangle to terminal
    Returns:
        float: area of rectangle
    """
    while True:
        try:
            side_1 = input_figure_parameter()
            side_2 = input_figure_parameter()
        except LessThenZeroError as e:
            print(f"Figure parameter can not be less than zero\n{e}")
        else:
            area = calculate_rectangle_area(side_1, side_2)
            print(f"Rectangle area: {area}")
            return area

def action_if_triangle() -> float:
    """
    Function to perform action if user have chosen triangle, prints triangle area to terminal
    Returns:
        float: area of triangle
    """
    while True:
        try:
            side_1 = input_figure_parameter()
            side_2 = input_figure_parameter()
            side_3 = input_figure_parameter()
            validate_triangle_sides(side_1, side_2, side_3)

        except LessThenZeroError as e:
            print(f"Figure parameter can not be less than zero\n{e}")
        except TriangleSidesError as e:
            print(f"Triangle sides are invalid one side always less than sum of two other\n{e}")
        else:
            area = calculate_triangle_area(side_1, side_2, side_3)
            print(f"Triangle area: {area}")
            return area

def action_if_circle() -> float:
    """
    Function to perform action if user have chosen circle, prints circle area to terminal
    Returns:
        float: area of circle
    """
    while True:
        try:
            radius = input_figure_parameter()
        except LessThenZeroError as e:
            print(f"Figure parameter can not be less than zero\n{e}")
        else:
            area = calculate_circle_area(radius)
            print(f"Circle area: {area}")
            return area

def input_figure_type() -> int:
    """
    Function that asks user to enter figure type
    Returns:
        int: number of chosen figure
    Raises:
        ValueError: if figure number not supported
    """
    print("Enter figure type:\nEnter 1 if rectangle:\nEnter 2 if triangle\nEnter 3 if circle\n> ")
    user_figure = int(input())
    if user_figure not in {1, 2, 3}:
        raise ValueError("Invalid figure number")
    return user_figure

def main():

    figure_type_area = {
        1: action_if_rectangle,
        2: action_if_triangle,
        3: action_if_circle
    }

    while True:
        try:
            user_figure = input_figure_type()
        except ValueError as e:
            print(f"{e}")
        else:
            figure_type_area[user_figure]() 
            return None
    
if __name__ == "__main__":
    main()


