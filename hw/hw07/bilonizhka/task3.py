def calculateNumberOfChars(text):
    """Calculates number of characters in given text"""
    output = {}
    for i in text:
        curV = output.get(i, 0)
        output[i] = curV + 1
    return output
