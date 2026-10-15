def higher_number(num1, num2):
    """
    returns the largest number of numbers
    
    """
    if num1 > num2:
        return num1
    else :
        return num2

first_number = float(input("Enter your first number:"))
second_number = float(input("Enter your second number:"))

result = higher_number(first_number, second_number)
print(result)