def compare_numbers(first_num: int, second_num: int) -> int:
    """
    This function compares two numbers from input
    and returns the largest one

    args:
        first_num - int
        second_num - int
    output: int
    """

    if first_num > second_num:
        return f"{first_num} is the largest"
    elif first_num < second_num:
        return f"{second_num} is the largest"
    return "Numbers are equal"
