def calc_char_num(word: str) -> dict:
    """
    This function calculates the
    number of characters in input

    args:
        word - str
    output: dict
    """

    output = {}
    for letters in word:
        output[letters] = output.get(letters, 0) + 1
    return output
