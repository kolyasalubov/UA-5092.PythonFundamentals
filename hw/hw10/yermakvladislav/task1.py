class Polygon():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        


class Rectangle(Polygon):
    def square(self):
        s = self.a * self.b
        return s
    
    
my_rectangle = Rectangle(1, 2)
result = my_rectangle.square()
print("Result:", result)