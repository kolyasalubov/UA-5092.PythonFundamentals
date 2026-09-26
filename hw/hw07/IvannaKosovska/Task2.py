import math

def rectangleArea(length, width):
    """
    This function calculates the area of rectangle
    """
    return length * width

def triangleArea(base, height):
    """
    This function calculates the area of triangle
    """
    return base * height / 2

def circleArea(radius):
    """
    This function calculates the area of circle
    """
    return math.pi * radius ** 2

userChoice = input("Please select the figure whose area you'd like to calculate: rectangle, triangle, or circle: ").lower()

while userChoice != "rectangle" and userChoice != "triangle" and userChoice != "circle":
    userChoice = input("Sorry, unkown figure entered." \
    " Please select the figure whose area you'd like to calculate: rectangle, triangle, or circle: ").lower()
    
if userChoice == "rectangle":
    length = float(input("Please enter the length: "))
    width = float(input("Please enter the width: "))
    print(round(rectangleArea(length, width), 2))

elif userChoice == "triangle":
    height = float(input("Please enter the height: "))
    base = float(input("Please enter the base: "))
    print(round(triangleArea(base, height), 2))

else:
    radius = float(input("Please enter the radius: "))
    print(round(circleArea(radius), 2))

