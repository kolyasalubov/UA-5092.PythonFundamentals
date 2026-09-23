# Write a function that calculates the number 
# of characters included in given string
# input: "hello"
# output: {"h":1, "e":1,"l":2,"o":1}


def count_characters(text: str) -> dict[str, int]:
    """
    Calculate the number of characters included in a given string.

    text: input string to count characters from
    """
    result = {}
    for char in text:
        result[char] = result.get(char, 0) + 1
    return result
