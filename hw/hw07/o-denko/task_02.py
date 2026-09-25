# Write a program that calculates the area of a rectangle, triangle
# and circle (write three functions to calculate the area. And call
# them in the main program depending on the user's choice)

import math


def calculate_area_rectangle(a: int | float, b: int | float) -> int | float:
    """
    Calculate the area of a rectangle.

    a: length of the rectangle
    b: width of the rectangle
    """
    return a * b


def calculate_area_triangle(base: int | float, height: int | float) -> float:
    """
    Calculate the area of a triangle.

    base: base of the triangle
    height: height of the triangle
    """
    return 0.5 * base * height


def calculate_area_circle(radius: int | float) -> float:
    """
    Calculate the area of a circle.

    radius: radius of the circle
    """
    return math.pi * radius ** 2


def main():
    """
    Run the main program to calculate area based on user choice.
    """
    print("Choose a figure to calculate area:")
    print("1. Rectangle\n2. Triangle\n3. Circle")
    choice_function = input("Enter your choice (1-3): ")

    match choice_function:
        case "1":
            try:
                a = float(input("Enter length of the rectangle: "))
                b = float(input("Enter width of the rectangle: "))
                if a > 0 and b > 0:
                    print(calculate_area_rectangle(a, b))
                else:
                    print("Sides must be greater than zero.")
            except ValueError:
                print("Invalid input. Please enter numbers only.")
        case "2":
            try:
                base = float(input("Enter base of the triangle: "))
                height = float(input("Enter height of the triangle: "))
                if base > 0 and height > 0:
                    print(calculate_area_triangle(base, height))
                else:
                    print("Base and height must be greater than zero.")
            except ValueError:
                print("Invalid input. Please enter numbers only.")
        case "3":
            try:
                radius = float(input("Enter radius of the circle: "))
                if radius > 0:
                    print(calculate_area_circle(radius))
                else:
                    print("Radius must be greater than zero.")
            except ValueError:
                print("Invalid input. Please enter numbers only.")
        case _:
            print("Incorrect data entered")


main()
