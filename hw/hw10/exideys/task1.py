class Polygon:
    """Represent a polygon with a collection of sides."""

    def __init__(self, *args: float | int) -> None:
        """
        Initialize a polygon with the given side values.

        Args:
            *args: Side values of the polygon.
        """
        self.sides: list[float | int] = list(args)


class Rectangle(Polygon):
    """Represent a rectangle with width and height."""

    def __init__(self, width: float | int, height: float | int) -> None:
        """
        Initialize a rectangle with width and height.

        Args:
            width: Width of the rectangle.
            height: Height of the rectangle.
        """
        super().__init__(width, height)

    def area(self) -> float | int:
        """
        Calculate the area of the rectangle.

        Returns:
            The area of the rectangle.
        """
        return self.sides[0] * self.sides[1]