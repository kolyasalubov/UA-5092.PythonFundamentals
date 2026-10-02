def return_largest_number(num1: int, num2: int) -> int:
    """
    Returns the largest of two numbers.

    Args:
        num1 (int): The first number.
        num2 (int): The second number.

    Returns:
        int: The larger of the two numbers.
    """
    return num1 if num1 >= num2 else num2
