def count_characters(text):
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    return counts
