word = input("Write a word: ")


def count_characters(word):
    characters = {}

    for letter in word:
        if letter in characters:
            characters[letter] += 1
        else:
            characters[letter] = 1

    return characters

print(count_characters(word))