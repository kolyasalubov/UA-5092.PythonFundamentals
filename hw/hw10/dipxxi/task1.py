class Polygon:
    """Базовий клас для геометричного багатокутника."""

    def __init__(self, sides_amount: int, sides: list[float] | None = None) -> None:
        """Ініціалізує багатокутник із заданою кількістю сторін."""
        self.sides_amount = sides_amount
        self.sides = sides or []

    @staticmethod
    def input_positive_number(value_name: str = 'value') -> float:
        """Запитує позитивне число через консоль з валідацією."""
        while True:
            try:
                value = float(input(f"Enter {value_name} (positive number): "))
                if value > 0:
                    return value
                print(f"Invalid {value_name}, number should be above 0")
            except ValueError:
                print("Invalid input, please enter a valid number")

    def input_sides(self) -> None:
        """Запитує довжину кожної сторони багатокутника."""
        self.sides = [float(input(f"Enter side {i+1}: "))
                      for i in range(self.sides_amount)]


class Rectangle(Polygon):
    """Клас для прямокутника, що успадковує багатокутник."""

    def __init__(self) -> None:
        """Ініціалізує прямокутник з 4 сторонами."""
        super().__init__(4)
        self.height: float = 0.0
        self.width: float = 0.0

    def input_sides(self) -> None:
        """Запитує висоту та ширину, оновлюючи список сторін."""
        self.height = self.input_positive_number('height')
        self.width = self.input_positive_number('width')
        self.sides = [self.height, self.height, self.width, self.width]

    def calculate_area(self) -> float:
        """Обчислює та повертає площу прямокутника."""
        return self.width * self.height


if __name__ == '__main__':
    rect = Rectangle()
    rect.input_sides()
    print(f"Rectangle area is: {rect.calculate_area():.2f}")



