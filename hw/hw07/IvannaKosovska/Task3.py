def calculateNumberOfCharacter(text):
    """
    This function calculates number of characters in the word entered by user
    """
    textDict = {}
    for char in text:
        if char in textDict:
            textDict[char] = textDict[char] + 1
        else:
            textDict[char] = 1
    return textDict

word = input("Enter some word:")
print(calculateNumberOfCharacter(word))



    






