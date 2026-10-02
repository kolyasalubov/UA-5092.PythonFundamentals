import math

def calculate_area_rectangle(length, width):
    if length <= 0 or width <= 0:
        print("Length and width must be positive.")
        return None
    return length * width

def calculate_area_triangle(base, height):
    if base <= 0 or height <= 0:
        print("Base and height must be positive.")
        return None
    return 0.5 * base * height

def calculate_area_circle(radius):
    if radius <= 0:
        print("Radius must be positive.")
        return None
    return math.pi * radius ** 2

def run_area_calculator():
    print("Choose a shape to calculate its area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == "1":
        length = int(input("Enter length: "))
        width = int(input("Enter width: "))
        print(f"Area of rectangle: {calculate_area_rectangle(length, width)}")
    elif choice == "2":
        base = int(input("Enter base: "))
        height = int(input("Enter height: "))
        print(f"Area of triangle: {calculate_area_triangle(base, height)}")
    elif choice == "3":
        radius = int(input("Enter radius: "))
        print(f"Area of circle: {calculate_area_circle(radius)}")
    else:
        print("Invalid choice.")

run_area_calculator()