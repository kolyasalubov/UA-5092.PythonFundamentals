from __future__ import annotations

class Polygon:
    """
    Base class for all polygons.
    """

    def __init__(self, n_sides: int) -> None:
        if n_sides < 3:
            raise ValueError("A polygon must have at least 3 sides.")
        self.n_sides = n_sides


class Rectangle(Polygon):
    """
    A class representing a rectangle.
    """

    def __init__(self, width: float | int, height: float | int) -> None:
        if width <= 0 or height <= 0:
            raise ValueError("Sides must be positive numbers.")
        super().__init__(4)
        self.width = width
        self.height = height

    def area(self) -> float | int:
        """
        Calculate and return the area of the rectangle.
        """
        return self.width * self.height

    def __repr__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"


if __name__ == '__main__':
    rect = Rectangle(25, 13)
    print(f"Number of sides: {rect.n_sides}")
    print(f"Area of rectangle: {rect.area()}")
