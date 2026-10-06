def count_chars(text: str) -> dict[str, int]:
    """
    This function counts how many times each character occurs in a string.
    Args:
        text: The string to analyze.
    Returns:
        A dictionary where keys are characters and values are their counts.
    """
    counts = {}
    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts


user_text = input("Type your text: ")
print(count_chars(user_text))
