def calculate_characters_in_string(string: str) -> dict:
    """Calculate the number of occurrences of each character in a string.

    Args:
        string (str): The input string.

    Returns:
        dict: A dictionary where keys are characters
            and values are their counts.
    """
    characters_count = {}
    for i in string:
        if i in characters_count:
            characters_count[i] += 1
        else:
            characters_count[i] = 1
    return characters_count