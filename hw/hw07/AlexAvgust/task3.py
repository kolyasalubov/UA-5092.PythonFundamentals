def calculate_occurs_leters(string: str) -> dict:
    """
    Calculate the occurrences of each letter in a given string.

    Args:
        string (str): The input string.
    """
    occurrences = {}
    for char in string:
        if char.isalpha():
            char_lower = char.lower()
            occurrences[char_lower] = occurrences.get(char_lower, 0) + 1
    return occurrences


print(calculate_occurs_leters("Hello, World!"))
