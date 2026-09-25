def get_dict_of_unique_characters(string: str) -> dict[str, int]:
    """
    This function returns a dictionary with the number of occurrences of each character in a string.
    """
    char_counts = {}
    for char in string:
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts


print(get_dict_of_unique_characters("!hellooo!!"))