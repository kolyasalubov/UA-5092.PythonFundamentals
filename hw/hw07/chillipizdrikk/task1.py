# Write a function that returns the largest number of two numbers
# (use DocStrings documentation strings in the function).

def largest_number(a: int | float, b: int | float) -> int | float:
    '''
    Function that returns the largest of two numbers
    Args:
        a: first number
        b: second number
    Returns:
        The largest number
    '''
    return max(a, b)