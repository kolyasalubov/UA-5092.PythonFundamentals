"""
Task 1. Write a function that returns the largest number of two numbers.
"""


def find_largest(a: int, b: int) -> int:
    """
    Returns the largest of two numbers.

    Parameters:
    a (int): first number
    b (int): second number

    Returns:
    int: the larger of a and b
    """
    if a > b:
        return a
    else:
        return b


if __name__ == "__main__":
    print(find_largest(10, 25))  # 25
    print(find_largest(7, 3))    # 7
