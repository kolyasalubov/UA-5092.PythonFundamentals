def comparison_of_numbers():
    """
    Returns the larger of two numbers or a message if they are equal
    """
    
    a = int(input("The first number: "))
    b = int(input("The second number: "))
    
    if a > b:
        result = a
    elif a == b:
        result = "The numbers are equal"
    else:
        result = b
        
    return result

print (comparison_of_numbers())
