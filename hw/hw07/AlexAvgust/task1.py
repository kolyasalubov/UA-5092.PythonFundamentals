def the_largest_num(num1: int , num2: int) -> int:
    '''
    args:
        num1: int - first number
        num2: int - second number
    return:
        int - the largest number between num1 and num2
    '''
    return num1 if num1 > num2 else num2

print(the_largest_num(1,2))
