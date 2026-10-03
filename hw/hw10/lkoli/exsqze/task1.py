class Polygon:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Rectangle(Polygon):
    def area(self):
        return self.width * self.height

rect = Rectangle(5, 10)
print(f"Rectangle area: {rect.area()}")