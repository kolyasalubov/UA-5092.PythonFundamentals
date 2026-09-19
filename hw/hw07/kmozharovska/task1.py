def return_largest_num(num1: int | float, num2: int | float) -> int | float:
    """
    Return the largest number of two numbers.
    input parameters:
        num1 - int or float
        num2 - int or float
    output:
        int or float
    """
    if not (isinstance(num1, (int, float, bool))
            and isinstance(num2, (int, float, bool))):
        raise TypeError("Both arguments should be int or float data type.")

    return max(num1, num2)


return_largest_num(1, 0) #1
return_largest_num(-1, -5) #-1
return_largest_num(1, 100.0) #100.0
return_largest_num("5", -1) #TypeError
return_largest_num(5, "0") #TypeError
