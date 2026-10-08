def number_of_letters():
    word = str(input("your word: "))
    result = {}

    for l in word:
        if l not in result:
            result[l] = (word.count(l))

    return result

print (number_of_letters())
