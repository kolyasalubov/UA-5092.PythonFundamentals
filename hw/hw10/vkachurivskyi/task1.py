class Polygon:
    """Базовий клас для багатокутників"""
    def __init__(self, sides):
        self.sides = sides

class Rectangle(Polygon):
    """Клас прямокутника, що успадковується від багатокутника"""
    def __init__(self, width, height):
        Polygon.__init__(self, [width, height, width, height])
        self.width = width
        self.height = height

    def get_square(self):
        """Обчислює та повертає площу прямокутника"""
        return self.width * self.height

rect_width = float(input("Введіть ширину прямокутника: "))
rect_height = float(input("Введіть висоту прямокутника: "))

my_rectangle = Rectangle(rect_width, rect_height)
result = my_rectangle.get_square()

print(f"Площа прямокутника: {result}")