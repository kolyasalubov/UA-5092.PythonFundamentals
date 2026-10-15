class Polygon:
    """
    A class representing a generic polygon.
    """

    def __init__(self, sides: int, values: list[float] | None = None) -> None:
        """
        Initialize the polygon.

        :param sides: The number of sides of the polygon.
        :param values: A list of side lengths. If None, an empty list is created.
        """
        self.sides: int = sides
        self.values: list[float] = values if values is not None else []

    def input_values(self) -> None:
        """
        Prompt the user to enter the length of each side of the polygon.
        """
        self.values = []
        for i in range(self.sides):
            value: float = float(input(f"Enter value for side {i+1}: "))
            self.values.append(value)


class Rectangle(Polygon):
    """
    A class representing a rectangle that inherits from Polygon.
    """

    def __init__(self) -> None:
        """
        Initialize a rectangle with 2 core dimensions (length and width).
        """
        super().__init__(sides=2)

    def calculate_area(self) -> float:
        """
        Calculate the area of the rectangle.

        :return: The area of the rectangle as a float.
        :raises IndexError: If the side values have not been provided yet.
        """
        if len(self.values) < 2:
            raise IndexError("Please provide side lengths using input_values() before calculating.")
        
        return self.values[0] * self.values[1]


if __name__ == "__main__":
    r: Rectangle = Rectangle()
    r.input_values()
    area: float = r.calculate_area()
    print(f"The area of your rectangle is {area}")
