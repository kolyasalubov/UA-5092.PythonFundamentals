def word_calculator(word):
    result_dict = {}

    for letter in word:
        if  letter in result_dict:
            result_dict[letter] += 1
        else : 
            result_dict[letter] = 1
    return result_dict

user_word = input("Enter a word: ")
print(word_calculator(user_word))





