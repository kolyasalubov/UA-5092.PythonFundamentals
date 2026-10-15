from math import pi

print("Choose formula: \n1 - for rectangle \n2 - for triangle \n3 - for circle")
choose_formula = int(input("Your choise: "))

def calculate_circle_area(pi, r: int) -> float:
    """
    This function calculates the area of a circle

    args:
        r - int
    output: float
    """

    area = round(pi * r**2, 2)
    return f"The area of this circle is {area}"

def calculate_triangle_area(side_h: int, height: int) -> float:
    """
    This function calculates the area of a triangle

    args:
        side_h - int
        height - int
    output: float
    """

    area = round(0.5 * side_h * height, 2)
    return f"The area of this triangle is {area}"

def calculate_rectangle_area(side_a: int, side_b: int) -> int:
    """
    This function calculates the area of a rectangle

    args:
        side_a - int
        side_b - int
    output: int
    """

    area = side_a * side_b
    return f"The area of this rectangle is {area}"

if __name__ == "__main__":

    if choose_formula == 1:
        print(calculate_rectangle_area(int(input("Enter the first side: ")), int(input("Enter the second side: "))))
    elif choose_formula == 2:
        print(calculate_triangle_area(int(input("Enter the side: ")), int(input("Enter the height: "))))
    elif choose_formula == 3:
        print(calculate_circle_area(pi, int(input("Radius: "))))
    else:
        print("Incorrect input")
