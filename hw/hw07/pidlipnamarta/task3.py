def count_characters(text: str) -> dict[str, int]:
    """
    The function returns a dictionary containing the count of each character
    """
    counts: dict[str, int] = {}

    for character in text:
        counts[character] = counts.get(character, 0) + 1

    return counts


text = input("Input a row: ")
print(f"The number of characters: {count_characters(text)}")