import math


def get_rectangle_area(height, width):
    """Calculates the area of a rectangle"""
    return height * width


def get_triangle_area(height, width):
    """Calculates the area of a triangle"""
    return height * width / 2


def get_circle_area(radius):
    """Calculates the area of a circle"""
    return radius ** 2 * math.pi


def handle_rectangle_area():
    width = float(input("Enter width in millimiters: "))
    height = float(input("Enter height in millimiters: "))
    area = get_rectangle_area(width=width, height=height)
    print(f"Rectangle area: {area}")


def handle_triangle_area():
    width = float(input("Enter width in millimiters: "))
    height = float(input("Enter height in millimiters: "))
    area = get_triangle_area(width=width, height=height)
    print(f"Triangle area: {area}")


def handle_circle_area():
    radius = float(input("Enter radius in millimiters: "))
    area = get_circle_area(radius)
    print(f"Circle area: {round(area, 2)}")


def main():
    print("Please select shape to calculate area: ")
    print("  1. Rectangle")
    print("  2. Triangle")
    print("  3. Circle")

    user_input = input("Enter your shape (1-3): ")

    if user_input == '1':
        return handle_rectangle_area()
    elif user_input == '2':
        return handle_triangle_area()
    elif user_input == '3':
        return handle_circle_area()
    else:
        print("Unknown shape")


if __name__ == '__main__':
    main()
