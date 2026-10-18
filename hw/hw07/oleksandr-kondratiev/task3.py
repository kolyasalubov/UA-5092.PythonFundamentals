def count_chars(text):
    """Return a dict with the number of occurrences of each character in text."""
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    return counts


print(count_chars("hello"))
