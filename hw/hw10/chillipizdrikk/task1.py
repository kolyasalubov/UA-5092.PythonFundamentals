from abc import ABC, abstractmethod

"""Module for calculating shape`s areas"""


class Polygon(ABC):
    '''Base class for polygons'''

    def __init__(self, num_sides: int, sides: list[int | float] = None) -> None:
        """
        Initialize polygon.

        Args:
            num_sides: Number of sides needed to calculate area.
            sides: List of sides for polygon.
        """
        self.num_sides = num_sides
        self.sides = sides if sides is not None else []

    @abstractmethod
    def area(self):
        """Calculate polygon`s area."""
        pass


class Rectangle(Polygon):
    """Class for rectangles."""

    def __init__(self, sides: list[int | float] = None) -> None:
        """
        Initialize rectangle.
        
        Args:
            sides: List of two sides (width, height).
        """
        super().__init__(2, sides)

    def area(self):
        """Calculate rectangle`s area."""
        if len(self.sides) != self.num_sides:
            print("Incorrect sides input for rectangle")
            return 0
        return self.sides[0] * self.sides[1]
    
def check_number(number: str) -> float:
    """
    Function that checks if number is valid for calculations.

    Args: 
        number: Number entered by the user
    Returns:
        Value if it is valid
    """
    while True:
        try:
            value = float(input(number))
            if value <= 0:
                print("Value must be greater than zero.\n")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.\n")

def main():
    """
    Displays a menu to the user and calls the 
    appropriate functions for calculating areas.
    """
    while True:
        print("-" * 20 + "Menu" + "-" * 20)
        print("1. Calculate rectangle area")
        print("2. Exit\n")

        user_input = input("Choose your option: ").strip()
        if user_input == "1":
            width = check_number("Enter width: ")
            height = check_number("Enter height: ")
            rect = Rectangle([width, height])
            print(f"Area of rectangle [{rect}]: {rect.area()}\n")
        elif user_input == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1 or 2.\n")


if __name__ == "__main__":
    main()