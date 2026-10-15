def max_number(a: float, b: float) -> float :
    """"
    The function returns the largest number of two numbers
    """
    return a if a>=b else b

print(f"The largest number : {max_number(3,9)}")