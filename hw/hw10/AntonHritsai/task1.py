class Polygon:
    """Represents a polygon with multiple sides.
    """
    def __init__(self, *args: float | int) -> None:
        """Initializes a new instance of the Polygon class.

        Args:
            *args: The lengths of the sides of the polygon.
        """
        self.sides: list[float | int] = list(args)


class Rectangle(Polygon):
    """Represents a rectangle with width and height.
    """
    def __init__(self, width: float | int, height: float | int) -> None:
        """Initializes a new instance of the Rectangle class.

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
        """
        super().__init__(width, height)

    def find_area(self) -> float | int:
        """Returns the area of the rectangle.
        """
        return self.sides[0] * self.sides[1]