import math
 
 
def rectangle_area(length, width):
    """Return the area of a rectangle given its length and width."""
    return length * width
 
 
def triangle_area(base, height):
    """Return the area of a triangle given its base and height."""
    return 0.5 * base * height
 
 
def circle_area(radius):
    """Return the area of a circle given its radius."""
    return math.pi * (radius ** 2)


def main():
    print("Area Calculator")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
 
    choice = input("Choose a shape (1-3): ").strip()
 
    if choice == "1":
        length = int(input("Enter the length: "))
        width = int(input("Enter the width: "))
        area = rectangle_area(length, width)
        print(f"The area of the rectangle is {area:.2f}")
 
    elif choice == "2":
        base = int(input("Enter the base: "))
        height = int(input("Enter the height: "))
        area = triangle_area(base, height)
        print(f"The area of the triangle is {area:.2f}")
 
    elif choice == "3":
        radius = int(input("Enter the radius: "))
        area = circle_area(radius)
        print(f"The area of the circle is {area:.2f}")
    else:
        print("Invalid choice. Please run the program again and choose 1, 2, or 3.")


if (__name__ == "__main__"):
    main()
    