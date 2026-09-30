import areas


def get_positive_number(prompt: str) -> float:
    """
    Prompts the user for a positive number with input validation.
    """
    while True:
        try:
            val = float(input(prompt))
            if val <= 0:
                print("Error: Value must be greater than 0. Please try again.")
                continue
            return val
        except ValueError:
            print("Error: Please enter a valid number.")


def main():
    """
    Run the main program to calculate area based on user choice.
    """
    print("Choose a figure to calculate area:")
    print("1. Rectangle\n2. Triangle\n3. Circle")
    choice_function = input("Enter your choice (1-3): ")

    match choice_function:
        case "1":
            length = get_positive_number("Enter length of the rectangle: ")
            width = get_positive_number("Enter width of the rectangle: ")
            area = areas.calculate_area_rectangle(length, width)
            print(f"\nRectangle area: {area:.2f}")

        case "2":
            base = get_positive_number("Enter base of the triangle: ")
            height = get_positive_number("Enter height of the triangle: ")
            area = areas.calculate_area_triangle(base, height)
            print(f"\nTriangle area: {area:.2f}")

        case "3":
            radius = get_positive_number("Enter radius of the circle: ")
            area = areas.calculate_area_circle(radius)
            print(f"\nCircle area: {area:.2f}")
        case _:
            print("\nUnknown figure choice. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
