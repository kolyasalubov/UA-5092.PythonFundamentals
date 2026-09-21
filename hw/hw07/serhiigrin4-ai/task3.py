"""
Task 3. Write a function that calculates the number of characters
included in a given string.

Example:
input: "hello"
output: {"h": 1, "e": 1, "l": 2, "o": 1}
"""


def count_characters(text: str) -> dict:
    """
    Counts the occurrences of each character in a string.

    Parameters:
    text (str): the input string

    Returns:
    dict: a dictionary with characters as keys and their counts as values
    """
    result = {}
    for char in text:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result


if __name__ == "__main__":
    print(count_characters("hello"))
    # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
