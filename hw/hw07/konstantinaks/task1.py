def numbers(one, two):
    """
    Функція приймає 2 числа та повертає найбільше із них
    """
    if one > two:
        return one
    else:
        return two
result = numbers(10,20)
print(result)
