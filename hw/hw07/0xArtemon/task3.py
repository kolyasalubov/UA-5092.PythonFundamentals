def count_characters(input_str: str = "Hello World!") -> dict:
    """
    Calculates the number of characters included in the given string.

    Args:
        input_str (str, optional): The string to analyze. Defaults to "Hello World!".

    Returns:
        dict: A dictionary with characters as keys and their counts as values.
    """
    result = {}
    for character in input_str:
        result[character] = result.get(character, 0) + 1
    return result
