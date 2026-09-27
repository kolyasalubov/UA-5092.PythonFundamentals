from math import pi


def get_rectangle_area(width: float, height: float) -> float:
    """
    Calculate the rectangle area.
    """
    return width * height


def get_triangle_area(base: float, height: float) -> float:
    """
    Calculate the triangle area.
    """
    return 0.5 * base * height


def get_circle_area(radius: float) -> float:
    """
    Calculate the circle area.
    """
    return pi * radius ** 2


choice = input("Enter a figure's name: ").strip().lower()

if choice == "rectangle":
    width = float(input("Please provide a width value: "))
    height = float(input("Please provide a height value: "))
    print(get_rectangle_area(width, height))

elif choice == "triangle":
    base = float(input("Please provide a base value: "))
    height = float(input("Please provide a height value: "))
    print(get_triangle_area(base, height))

elif choice == "circle":
    radius = float(input("Please provide a radius value: "))
    print(get_circle_area(radius))

else:
    print("Unsupported figure.")