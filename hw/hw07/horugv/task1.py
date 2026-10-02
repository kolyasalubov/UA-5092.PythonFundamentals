def get_largest_number(a, b):
    """
    This function returns the largest number between two integers.
    Args:
        a: First integer
        b: Second integer
    Returns:
        The largest number between a and b
    """
    return max(a, b)

a = int(input())
b = int(input())
print(get_largest_number(a, b))