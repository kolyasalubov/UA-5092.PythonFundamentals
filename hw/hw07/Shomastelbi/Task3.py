def calc_char_num(word):
    """
    This function calculates the
    number of characters in input

    input: str
    output: dict
    """

    output = {}
    for letters in word:
        output[letters] = output.get(letters, 0) + 1
    return output    

print(calc_char_num("hello"))
