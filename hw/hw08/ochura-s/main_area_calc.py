from module_area_calc import circle_area, rectangle_area, triangle_area

FIGURES = {
    "1": ("rectangle", rectangle_area, ("side a", "side b")),
    "2": ("triangle", triangle_area, ("base a", "height h")),
    "3": ("circle", circle_area, ("radius r",)),
}


def read_dimension(name: str) -> float:
    """Ask the user for a dimension until a positive number is entered."""
    while True:
        try:
            value = float(input(f"Enter the {name}: "))
        except ValueError:
            print("Please enter a number.")
            continue

        if value <= 0:
            print("The value must be greater than zero.")
            continue

        return value


def main() -> None:
    """Run the menu, read the dimensions and print the calculated area."""
    print("Which area do you want to calculate?")
    for option, (figure, _, _) in FIGURES.items():
        print(f"  {option}. {figure.capitalize()}")

    choice = input("Enter your choice (1/2/3): ").strip()

    if choice not in FIGURES:
        print("There is no such option.")
        return

    figure, area_function, dimensions = FIGURES[choice]
    values = [read_dimension(name) for name in dimensions]
    print(f"The area of the {figure} is {round(area_function(*values), 2)}")


if __name__ == "__main__":
    main()
