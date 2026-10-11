from math import pow, pi
type Units = float | int
def area_of_circle(radius: Units) -> float:
    '''
    This function takes the radius of a circle as input and returns the area of the circle.
    The area is calculated using the formula: area = π * radius^2.
    The result is rounded to two decimal places.

    Args:
        radius (float | int): The radius of the circle.
    '''
    return round(pi * pow(radius, 2), 2)

def area_of_rectangle(length:Units, width: Units) -> float:
    '''
    This function takes the length and width of a rectangle as input and returns the area of the rectangle.
    The area is calculated using the formula: area = length * width.
    The result is rounded to two decimal places.

    Args:
        length (float | int): The length of the rectangle.
        width (float | int): The width of the rectangle.
    '''
    return round(length * width, 2)

def area_of_triangle(base:Units, height:Units) -> float:
    '''
    This function takes the base and height of a triangle as input and returns the area of the triangle.
    The area is calculated using the formula: area = 0.5 * base * height.
    The result is rounded to two decimal places.

    Args:
        base (float | int): The base of the triangle.
        height (float | int): The height of the triangle.
    '''
    return round(0.5 * base * height, 2)