def compare_numbers(first_num, second_num):
    """
    This function compares two numbers from input
    and returns the largest one
    """
    if first_num == second_num:
        return "Numbers are equal"
    if first_num > second_num:
        return f"{first_num} is the largest"
    return f"{second_num} is the biggest"


print(compare_numbers(5, 5))
print(compare_numbers(1, 3))
print(compare_numbers(5, 2))
