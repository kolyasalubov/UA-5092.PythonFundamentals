import math

def rectangle_area(width, height):
    """
    This function returns the area of a rectangle.
    """
    return width * height

def triangle_area(base, height):
    """
    This function returns the area of a triangle.
    """
    return 0.5 * base * height


def circle_area(radius):
    """
    This function returns the area of a circle.
    """
    return math.pi * radius ** 2


def main():
    shape = input("Enter the shape (rectangle, triangle, circle): ")
    match shape:
        case "rectangle":
            print("For rectangle area, you need to enter the width and height.")
            width = float(input("Enter the width: "))
            height = float(input("Enter the height: "))
            print(f"The area of the rectangle is {rectangle_area(width, height)}")
        case "triangle":
            print("For triangle area, you need to enter the base and height.")
            base = float(input("Enter the base: "))
            height = float(input("Enter the height: "))
            print(f"The area of the triangle is {triangle_area(base, height)}")
        case "circle":
            print("For circle area, you need to enter the radius.")
            radius = float(input("Enter the radius: "))
            print(f"The area of the circle is {circle_area(radius)}")
        case _:
            print("Invalid shape. Valid shape options: rectangle, triangle, circle.")

if __name__ == "__main__":
    main()