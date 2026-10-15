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
        self.height = 0
        self.width = 0

    def input_sides(self):
        self.height = self.input_positive_number('height')
        self.width = self.input_positive_number('width')
        self.sides = [self.height, self.height, self.width, self.width]

    def calculate_area(self):
        return self.width * self.height


if __name__ == '__main__':
    rect = Rectangle()
    rect.input_sides()
    print(f"Rectangle area is: {rect.calculate_area():.2f}")
