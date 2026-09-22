import areas

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
        result = areas.calculate_rectangle_area(side1, side2)
        print_area_result("Rectangle", result)
            
    elif choice == 2:
        base = float(input("Enter base value: "))
        height = float(input("Enter height value: "))
        result = areas.calculate_triangle_area(base, height)
        print_area_result("Triangle", result)
            
    elif choice == 3:
        radius = float(input("Enter radius value: "))
        result = areas.calculate_circle_area(radius)
        print_area_result("Circle", result)
            
    else:
        print("You entered wrong number! Try again!")

if __name__ == "__main__":
    make_your_choice()
