from math import pi, pow

def rectangle_area(length: float, width: float) -> float:
    '''
    Function that calculates an area of the rectangle
        Args:
            length: Length of rectangle
            width: Width of rectangle
        Returns:
            Area of the rectangle
    '''
    return length * width

def triangle_area(base: float, height: float) -> float:
    '''
    Function that calculates an area of the triangle
        Args:
            base: The bottom side of the triangle
            height: The straight, perpendicular line going from the base up to the 
            highest corner
        Returns:
            Area of the triangle
    '''
    return 0.5 * base * height

def circle_area(radius: float) -> float:
    '''
    Function that calculates an area of the circle
        Args:
            radius: Distance from the center of the circle to the outer edge
        Returns:
            Area of the circle
    '''
    return pi * pow(radius,2)

def check_number(number: str) -> float:
    '''
    Function that checks if number is valid for calculations
        Args: 
            number: Number entered by the user
        Returns:
            Value if it is valid
    '''
    while True:
        try:
            value = float(input(number))
            if value <= 0:
                print("Value must be greater than zero.\n")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.\n")
