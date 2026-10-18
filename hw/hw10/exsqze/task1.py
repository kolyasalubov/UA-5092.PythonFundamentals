from abc import ABC, abstractmethod

class Polygon(ABC):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    @abstractmethod
    def area(self):
        pass

class Rectangle(Polygon):
    def area(self):
        return self.width * self.height

rect = Rectangle(5, 10)
print(f"Rectangle area: {rect.area()}")