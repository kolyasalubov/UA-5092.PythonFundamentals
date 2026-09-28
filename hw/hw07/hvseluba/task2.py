from math import pi


def get_rectangle_area(width: float, height: float) -> float:
    """
    Calculate the rectangle area.
    """
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive.")
    return width * height


def get_triangle_area(base: float, height: float) -> float:
    """
    Calculate the triangle area.
    """
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive.")
    return 0.5 * base * height


def get_circle_area(radius: float) -> float:
    """
    Calculate the circle area.
    """
    if radius <= 0:
        raise ValueError("Radius must be positive.")
    return pi * radius ** 2


if __name__ == "__main__":
    choice = input("Enter a figure's name: ").strip().lower()

    if choice == "rectangle":
        width = float(input("Please provide a width value: "))
        height = float(input("Please provide a height value: "))
        print(get_rectangle_area(width, height))

    elif choice == "triangle":
        base = float(input("Please provide a base value: "))
        height = float(input("Please provide a height value: "))
        print(get_triangle_area(base, height))

    elif choice == "circle":
        radius = float(input("Please provide a radius value: "))
        print(get_circle_area(radius))

    else:
        print("Unsupported figure.")