import math

def rectangle_area(length, width):
    """
    This function calculates the area of rectangle
    """
    return length * width

def triangle_area(base, height):
    """
    This function calculates the area of triangle
    """
    return base * height / 2

def circle_area(radius):
    """
    This function calculates the area of circle
    """
    return math.pi * radius ** 2

user_choice = input("Please select the figure whose area you'd like to calculate: rectangle, triangle, or circle: ").lower()

while user_choice != "rectangle" and user_choice != "triangle" and user_choice != "circle":
    user_choice = input("Sorry, unkown figure entered." \
    " Please select the figure whose area you'd like to calculate: rectangle, triangle, or circle: ").lower()
    
if user_choice == "rectangle":
    length = float(input("Please enter the length: "))
    width = float(input("Please enter the width: "))
    print(round(rectangle_area(length, width), 2))

elif user_choice == "triangle":
    height = float(input("Please enter the height: "))
    base = float(input("Please enter the base: "))
    print(round(triangle_area(base, height), 2))

else:
    radius = float(input("Please enter the radius: "))
    print(round(circle_area(radius), 2))

