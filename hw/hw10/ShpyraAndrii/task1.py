from math import sqrt
from functools import reduce


class Polygon:
    def __init__(self, sides_amount, sides=None):
        self.sides_amount = sides_amount
        self.sides = sides or []

    @staticmethod
    def input_positive_number(value_name='value'):
        try:
            value = float(input(f"Enter {value_name} (positive number): "))
            if value > 0:
                return value
            raise ValueError()
        except ValueError:
            print(f"Invalid {value_name}, number should be above 0")
            return 0

    def input_sides(self):
        self.sides = [float(input(f"Enter side {i+1}: "))
                        for i in range(self.sides_amount)]


class Rectangle(Polygon):
    def __init__(self):
        super().__init__(4, [0, 0, 0, 0])

    def input_sides(self):
        height = self.input_positive_number('height')
        width = self.input_positive_number('width')
        self.sides = [height, height, width, width]

    def calculate_area(self):
        sides_product = reduce(lambda acc, value: acc * value, self.sides)
        return sqrt(sides_product)


if __name__ == '__main__':
    rect = Rectangle()
    rect.input_sides()
    print(f"Rectangle area is: {rect.calculate_area():.2f}")
