#Task2
#Write a program that calculates the area of a rectangle, triangle and circle
#(write three functions to calculate the area. 
# And call them in the main program depending on the user's choice).
print("Task2")
def triangle_area(a, h):
    """
    This function returns the area of a triangle
    input parameters: a - float/int (base), h - float/int (height)
    output: float
    """
    return 0.5 * a * h


def rectangle_area(a, b):
    """
    This function returns the area of a rectangle
    input parameters: a - float/int (width), b - float/int (length)
    output: float/int
    """
    return a * b


def circle_area(r):
    """
    This function returns the area of a circle
    input parameters: r - float/int (radius)
    output: float
    """
    return 3.14 * (r ** 2)

how_to_use = input("What area do you need: triangle (1), rectangle (2) or circle (3), use 1,2,3: ")

if how_to_use == "1":
    a = float(input("Enter base (a): "))
    h = float(input("Enter height (h): "))
    print(f"Triangle area: {triangle_area(a, h)}")

elif how_to_use == "2":
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    print(f"Rectangle area: {rectangle_area(a, b)}")

elif how_to_use == "3":
    r = float(input("Enter radius (r): "))
    print(f"Circle area: {circle_area(r)}")

else:
    print("Error! Please use 1, 2 or 3.")
