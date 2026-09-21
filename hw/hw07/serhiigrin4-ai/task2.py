"""
Task 2. Write a program that calculates the area of a rectangle,
triangle and circle (three functions, called depending on user's choice).
"""


def rectangle_area(width: float, height: float) -> float:
    """
    Calculates the area of a rectangle.

    Parameters:
    width (float): width of the rectangle
    height (float): height of the rectangle

    Returns:
    float: the area of the rectangle
    """
    return width * height


def triangle_area(base: float, height: float) -> float:
    """
    Calculates the area of a triangle.

    Parameters:
    base (float): base of the triangle
    height (float): height of the triangle

    Returns:
    float: the area of the triangle
    """
    return 0.5 * base * height


def circle_area(radius: float) -> float:
    """
    Calculates the area of a circle.

    Parameters:
    radius (float): radius of the circle

    Returns:
    float: the area of the circle
    """
    pi = 3.14159
    return pi * radius ** 2


def main() -> None:
    """
    Asks the user which shape to calculate and prints its area.
    """
    choice = input("Choose a shape (rectangle, triangle, circle): ")

    if choice == "rectangle":
        width = float(input("Enter width: "))
        height = float(input("Enter height: "))
        print("Area:", rectangle_area(width, height))
    elif choice == "triangle":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        print("Area:", triangle_area(base, height))
    elif choice == "circle":
        radius = float(input("Enter radius: "))
        print("Area:", circle_area(radius))
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
