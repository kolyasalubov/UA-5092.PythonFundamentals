print("Choose formula: \n1 - for rectangle \n2 - for triangle \n3 - for circle")
choose_formula = int(input("Your choise: "))

PI = 3.14

def calculate_circle_area(PI, r):
    """
    This function calculates the area of a circle
    """

    area = PI * r**2
    print(f"The area of this circle is {area}")

def calculate_triangle_area(side_h, height):
    """
    This function calculates the area of a triangle
    """

    area = 0.5 * side_h * height
    print(f"The area of this triangle is {area}")

def calculate_rectangle_area(side_a, side_b):
    """
    This function calculates the area of a rectangle
    """

    area = side_a * side_b
    print(f"The area of this rectangle is {area}")

if choose_formula == 1:
    calculate_rectangle_area(int(input("Enter the first side: ")), int(input("Enter the second side: ")))
elif choose_formula == 2:
    calculate_triangle_area(int(input("Enter the side: ")), int(input("Enter the height: ")))
elif choose_formula == 3:
    calculate_circle_area(PI, int(input("Radius: ")))
else:
    print("Incorrect input")
