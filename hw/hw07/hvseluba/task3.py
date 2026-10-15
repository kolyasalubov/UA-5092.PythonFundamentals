def count_characters(text: str) -> dict[str, int]:
    """
    Count the occurrences of each character in a string.
    """
    characters = {}
    text_normalized = text.strip().lower()

    for char in text_normalized:
        characters[char] = characters.get(char, 0) + 1

    return characters