def get_max_number(a, b):
    """Return the larger of two numbers."""
    return max(a, b)

def rectangle_area(a, b):
    """Return the area of a rectangle given its length and width."""
    return a * b

def count_chars(string):
    """Return the number of occurrences of each character."""
    char_count = {}
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count