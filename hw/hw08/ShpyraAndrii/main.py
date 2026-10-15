from area_calculations import get_circle_area, get_rectangle_area, get_triangle_area


def handle_rectangle_area():
    width = float(input("Enter width in millimeters: "))
    height = float(input("Enter height in millimeters: "))
    if width <= 0 or height <= 0:
        print("Width and height should be positive numbers")
        return
    area = get_rectangle_area(width=width, height=height)
    print(f"Rectangle area: {round(area, 2)} mm²")


def handle_triangle_area():
    base = float(input("Enter base in millimeters: "))
    height = float(input("Enter height in millimeters: "))
    if base <= 0 or height <= 0:
        print("Base and height should be positive numbers")
        return
    area = get_triangle_area(base=base, height=height)
    print(f"Triangle area: {round(area, 2)} mm²")


def handle_circle_area():
    radius = float(input("Enter radius in millimeters: "))
    if radius <= 0:
        print("Radius should be positive number")
        return
    area = get_circle_area(radius)
    print(f"Circle area: {round(area, 2)} mm²")


def main():
    print("Please select shape to calculate area: ")
    print("  1. Rectangle")
    print("  2. Triangle")
    print("  3. Circle")

    user_input = input("Enter your shape (1-3): ")

    if user_input == '1':
        handle_rectangle_area()
    elif user_input == '2':
        handle_triangle_area()
    elif user_input == '3':
        handle_circle_area()
    else:
        print("Unknown shape")


if __name__ == '__main__':
    main()
