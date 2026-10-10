class Polygon:
    """Represent a polygon with a width and height."""
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Rectangle(Polygon):
    """Calculate the area of a rectangle."""
    def calculate_area(self):
        return self.width * self.height

if __name__ == "__main__":
    rectangle = Rectangle(5, 10)
    print("Rectangle area:", rectangle.calculate_area())