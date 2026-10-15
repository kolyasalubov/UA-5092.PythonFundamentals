def largest_num_of_two(x, y):
    """
    This function returns the largest of two numbers.
    Args:
        x: The first number.
        y: The second number.
    Returns:
        The largest of the two numbers (if they are equal, that number).
    """
    if x > y:
        return x
    return y


try:
    first = float(input("Type first number: "))
    second = float(input("Type second number: "))
    print(f"The largest number is: {largest_num_of_two(first, second)}")
except ValueError:
    print("Invalid input. Please enter a valid number.")