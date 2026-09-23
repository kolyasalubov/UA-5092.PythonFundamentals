import area_calculator as acalc


def run_area_calculator():
    """Run the area calculator."""
    acalc.figure = input(
        "Enter a figure (rectangle, triangle, circle): ").lower()

    match(acalc.figure):
        case "rectangle":
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            return acalc.figure, acalc.calculate_rectangle_area(length, width)
        case "triangle":
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            return acalc.figure, acalc.calculate_triangle_area(base, height)
        case "circle":
            radius = float(input("Enter radius: "))
            return acalc.figure, acalc.calculate_circle_area(radius)
        case _:
            raise ValueError(f"Unknown figure: {acalc.figure}")


if __name__ == "__main__":
    figure, area = run_area_calculator()
    print(f"The area of your {figure} equals {area}.")
