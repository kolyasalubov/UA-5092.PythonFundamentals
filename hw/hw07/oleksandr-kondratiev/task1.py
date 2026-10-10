def max_of_two(a, b):
    """Return the larger of two numbers.

    Args:
        a: First number.
        b: Second number.

    Returns:
        The larger of a and b.
    """
    return max(a, b)


x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
print(f"The largest number is: {max_of_two(x, y)}")
