import math


def rectangle_area(width, height):
    """Return the area of a rectangle."""
    return width * height


def triangle_area(base, height):
    """Return the area of a triangle."""
    return 0.5 * base * height


def circle_area(radius):
    """Return the area of a circle."""
    return math.pi * radius ** 2


def main():
    print("Choose a figure: 1 - rectangle, 2 - triangle, 3 - circle")
    choice = input("Your choice: ").strip()

    if choice == "1":
        width = float(input("Width: "))
        height = float(input("Height: "))
        print(f"Rectangle area: {rectangle_area(width, height)}")
    elif choice == "2":
        base = float(input("Base: "))
        height = float(input("Height: "))
        print(f"Triangle area: {triangle_area(base, height)}")
    elif choice == "3":
        radius = float(input("Radius: "))
        print(f"Circle area: {circle_area(radius):.2f}")
    else:
        print("Invalid choice")


main()
