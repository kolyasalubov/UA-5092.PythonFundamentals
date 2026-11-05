from tools.inputnumber import input_number

def check_if_number(number:int|float) -> None:
    """
    Checks if given value a nuber, if not raises error

    Args:
        number (int|float): Number to check
    Raises:
        ValueError: value is not a number
    """

    if not isinstance(number, (int, float)):
        raise ValueError(f"Value {number} is not a number, it's {type(number)}")
    return None

def define_largest_number(number_1: int|float, number_2: int|float) -> int|float:
    """
    This function finds the largest number from two given
    
    Args:
        number_1 (int|float): First number to compare
        number_2 (int|float): Second number to compare
    Returns:
        int|float: largest number from two given

    """
    check_if_number(number_1)
    check_if_number(number_2)
    return number_1 if number_1 > number_2 else number_2

def main() -> None:
    number_1 = input_number()
    number_2 = input_number()
    try:
        largest_number = define_largest_number(number_1, number_2)
    except ValueError as e:
        print(f"Compared values are not numbers!\n{e}")
        return None
    else:
        print(f"Largest number is {largest_number}")
    return None

if __name__ == '__main__':
    main()
