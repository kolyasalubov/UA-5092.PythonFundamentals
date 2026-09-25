def return_largest_num(num1: float, num2: float) -> float:
    """
    Return the largest number of two numbers.
    Args:
        num1 - float
        num2 - float
    Returns: float
    """

    return max(num1, num2)


if __name__ == "__main__":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print(f"{return_largest_num(num1, num2)} is the largest number.")
