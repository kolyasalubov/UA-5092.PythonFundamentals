import area_calculator as acalc


def run_area_calculator(figure: str) -> float:
    """
    Run the area calculator.
    Args: figure - str
    Returns: float
    """

    match(figure):
        case "rectangle":
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            return acalc.calculate_rectangle_area(length, width)
        case "triangle":
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            return acalc.calculate_triangle_area(base, height)
        case "circle":
            radius = float(input("Enter radius: "))
            return acalc.calculate_circle_area(radius)
        case _:
            raise ValueError(f"Unknown figure: {figure}")


if __name__ == "__main__":
    figure = input("Enter a figure (rectangle, triangle, circle): ").lower()
    print(f"The area of your {figure} equals {run_area_calculator(figure)}.")
