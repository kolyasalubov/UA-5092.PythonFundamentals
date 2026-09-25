# Write a function that calculates the number 
# of characters included in given string
# input: "hello"
# output: {"h":1, "e":1,"l":2,"o":1}

def calculate_characters(word: str) -> dict[str, int]:
    '''
    Function that calculates the number of characters included in given string
    Args:
        word: Inputed string 
    Returns:
        Dictionary with character and the number of times it appears in the word
    '''
    result = {}
    for char in word:
        result[char] = result.get(char, 0) + 1

    return result