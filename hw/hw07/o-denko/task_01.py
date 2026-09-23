# Write a function that returns the largest number of two numbers
# (use DocStrings documentation strings in the function).

def get_max(a: int | float, b: int | float) -> int | float:
    """
    Return the largest of two numbers.
    """
    return max(a, b)
