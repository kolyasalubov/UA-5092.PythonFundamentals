import functools
from tools.errors import LessThenZeroError

def validate_figure_parameter(parameter: int|float) -> None:
    """
    Function validates figure parameter (side or radius) and throws error if it's less then or equal to 0
    Args:
        parameter (int|float)
    Raises:
        LessThenZeroError: custom error class when figure parameter less then 0
    """
    if parameter <= 0:
        raise LessThenZeroError(f"{parameter} <= 0! Figure parameter cannot be less then or eaqual to zero")
    return None

def figure_parameter(func):
    """
    Function to wrap input_number and add figure parameter validation, parameter should not be less then 0
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        parameter = func(*args, **kwargs)
        validate_figure_parameter(parameter)
        return parameter
    return wrapper

def input_number() -> int|float:
    """
    Function asks user to enter value and converts it to int or float, if error - prints error
    Returns:
        number (int|float):: Converted to int or float input from user
    """
    while True:
        print("Enter number:\n> ")
        value = input()
        number = 0
        change_type = int
        if value.count(".") > 0:
            change_type = float
        try:
            number = change_type(value)
        except ValueError as e:
            print(f"Entered value is not a number or format is invalid!\n{e}\nTry again!")
        else:
            return number

@figure_parameter
def input_figure_parameter():
    """
    Function to input figure parameter from terminal
    """
    return input_number()