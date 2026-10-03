from abc import ABC, abstractmethod
from collections import Counter
from math import sqrt

"""
Program for calculating the perimeter and area of rectangles and triangles.
"""


class Polygon(ABC):
    """Base class for polygons."""
    def __init__(self, sides_count: int) -> None:
        """Initialize a polygon with the specified number of sides."""
        self.sides_count = sides_count
        self.sides = [0.0] * sides_count

    def input_sides(self) -> None:
        """Read and validate positive side lengths from user input."""
        for i in range(self.sides_count):
            while True:
                try:
                    side_value = float(input(f"Enter side {i + 1}: "))
                    if side_value <= 0:
                        print("Side must be greater than zero.")
                        continue
                    break
                except ValueError:
                    print("Please enter a valid number.")
            self.sides[i] = side_value

    def calc_perimeter(self) -> float:
        """Calculate and return the polygon's perimeter."""
        return sum(self.sides)

    @abstractmethod
    def calc_area(self) -> float:
        """Calculate and return the polygon's area."""


class Rectangle(Polygon):
    """Class for rectangles."""
    def __init__(self) -> None:
        """Initialize a rectangle with four sides."""
        super().__init__(4)

    def input_sides(self) -> None:
        """Read sides and validate that they form a rectangle."""
        while True:
            super().input_sides()
            sides = Counter(self.sides).values()
            is_square = len(sides) == 1
            is_rectangle = (len(sides) == 2 and
                            all(value == 2 for value in sides))
            if is_square or is_rectangle:
                break
            else:
                print(f"The sides {self.sides} cannot form a rectangle.")
                print("Please enter valid sides.")

    def calc_area(self) -> float:
        """Calculate and return the rectangle's area."""
        return max(self.sides) * min(self.sides)


class Triangle(Polygon):
    """Class for triangles."""
    def __init__(self) -> None:
        """Initialize a triangle with three sides."""
        super().__init__(3)

    def input_sides(self) -> None:
        """Read sides and validate that they form a triangle."""
        while True:
            super().input_sides()
            largest_side = max(self.sides)
            other_sides = sum(self.sides) - largest_side
            if largest_side < other_sides:
                break
            else:
                print(f"The sides {self.sides} cannot form a triangle.")
                print("Please enter valid sides.")

    def calc_area(self) -> float:
        """Calculate and return the triangle's area using Heron's formula."""
        side_a, side_b, side_c = self.sides
        semi_perimeter = self.calc_perimeter() / 2
        return sqrt(semi_perimeter * (semi_perimeter - side_a) *
                    (semi_perimeter - side_b) * (semi_perimeter - side_c))


def main() -> None:
    """Run the interactive polygon calculator."""
    while True:
        choice = input(
            "Choose figure (rectangle or triangle): ").strip().lower()

        if choice == "rectangle":
            rect = Rectangle()
            rect.input_sides()
            print(f"Your rectangle's perimeter is {rect.calc_perimeter()}")
            print(f"Your rectangle's area is {rect.calc_area()}")
            break
        elif choice == "triangle":
            triangle = Triangle()
            triangle.input_sides()
            print(f"Your triangle's perimeter is {triangle.calc_perimeter()}")
            print(f"Your triangle's area is {triangle.calc_area()}")
            break
        else:
            print("Invalid figure. Please try again.")


if __name__ == "__main__":
    main()
