def count_letters(word):
    """
    This function calculate the number of characters include in given string
    """
    word = word.lower()

    result = {}

    for letter in word:
        if letter not in result:
            result[letter] = 1
        else:
            result[letter] += 1

    return result

slovo = str(input('Type a word: '))

print(count_letters(slovo))