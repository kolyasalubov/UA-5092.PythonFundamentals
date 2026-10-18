class Polygon:
    """A class representing a polygon."""

    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height


class Rectangle(Polygon):
    """A class representing a rectangle that inherits from Polygon."""

    def area(self) -> float:
        return self.width * self.height


rectangle = Rectangle(5, 4)
print(rectangle.area())