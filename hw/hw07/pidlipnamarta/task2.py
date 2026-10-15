from math import pi

def rectangle_area (length: float, width: float) -> float:
    """
   The function returns the area of a rectangle given its length and width
   """
    return length * width


def triangle_area(base: float, height: float) -> float:
    """
    The function returns the area of a triangle given its base and height
    """
    return base * height / 2


def circle_area(radius: float) -> float:
    """The function returns the area of a circle given its radius
    """
    return pi * radius ** 2


def main() -> None:
    """
    The function calculates the area of the shape depending on the user's choice
    """
    choice = input(
        "Choose the figure: 1 - rectangle, 2 - triangle, 3 - circle: "
    )

    if choice == "1":
        length = float(input("Input lenght: "))
        width = float(input("Input width: "))
        area = rectangle_area(length, width)
    elif choice == "2":
        base = float(input("Input base: "))
        height = float(input("Input height: "))
        area = triangle_area(base, height)
    elif choice == "3":
        radius = float(input("Input radius: "))
        area = circle_area(radius)
    else:
        print("Wrong choice")
        return

    print(f"The area of the shape: {area:.2f}")

main()