class Polygon:
    """
    A polygon described by the lengths of its sides.
    """

    def __init__(self, *sides):
        self.sides = sides

    def perimeter(self):
        return sum(self.sides)


class Rectangle(Polygon):
    """
    A rectangle is a polygon with two pairs of equal sides.
    """

    def __init__(self, width, height):
        super().__init__(width, height, width, height)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


rectangle = Rectangle(4, 5)
print(f"Rectangle perimeter: {rectangle.perimeter()}")
print(f"Rectangle area: {rectangle.area()}")
