# Write a program that calculates the area of a rectangle, triangle
# and circle (write three functions to calculate the area. And call
# them in the main program depending on the user's choice)

from math import pi

def rectangle_area(length: float, width: float) -> float:
    '''
    Function that calculates an area of the rectangle
        Args:
            length: Length of rectangle
            width: Width of rectangle
        Returns:
            Area of the rectangle
    '''
    return length * width

def triangle_area(base: float, height: float) -> float:
    '''
    Function that calculates an area of the triangle
        Args:
            base: The bottom side of the triangle
            height: The straight, perpendicular line going from the base up to the 
            highest corner
        Returns:
            Area of the triangle
    '''
    return 0.5 * base * height

def circle_area(radius: float) -> float:
    '''
    Function that calculates an area of the circle
        Args:
            radius: Distance from the center of the circle to the outer edge
        Returns:
            Area of the circle
    '''
    return pi * radius ** 2

def main():
    '''
    The program's entry point. Displays a menu to the user and calls the 
    appropriate functions for calculating areas.
    '''
    while True:
        print(f"{'-' * 30} Areas menu {'-' * 30}")
        print("1. Calculate rectangle area")
        print("2. Calculate triangle area")
        print("3. Calculate circle area")
        print("4. Quit")
    
        user_input = input("\nChoose your option: ")
    
        match user_input:
            case "1":
                try:
                    length = float(input("Enter length: "))
                    width = float(input("Enter width: "))
                    print(f"Area of your rectangle is: {rectangle_area(length, width)}\n")
                except ValueError:
                    print("Please enter a valid number.\n")
            case "2":
                try:
                    base = float(input("Enter base: "))
                    height = float(input("Enter height: "))
                    print(f"Area of your triangle is: {triangle_area(base, height)}\n")
                except ValueError:
                    print("Please enter a valid number.\n")
            case "3":
                try:
                    radius = float(input("Enter radius: "))
                    print(f"Area of your circle is: {circle_area(radius)}\n")
                except ValueError:
                    print("Please enter a valid number.\n")
            case "4":
                break
            case _:
                print("Invalid input. Try again\n")

main()