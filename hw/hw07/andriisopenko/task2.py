import math

def rectangle(length: float, width: float) -> float:
    return length * width
def triangle(base: float, height: float) -> float:
    return 0.5 * base * height
def circle(radius: float) -> float:
    return math.pi * radius ** 2

choice = input("Choose shape (rectangle, triangle, circle): ")
if choice == "rectangle":
    length = float(input("Length: "))
    width = float(input("Width: "))
    print(rectangle(length, width))
elif choice == "triangle":
    base = float(input("Base: "))
    height = float(input("Height: "))
    print(triangle(base, height))
elif choice == "circle":
    radius = float(input("Radius: "))
    print(circle(radius))
else:
    print("Invalid choice")