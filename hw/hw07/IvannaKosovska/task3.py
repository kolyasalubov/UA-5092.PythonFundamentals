def calculate_number_of_character(text):
    """
    This function calculates number of characters in the word entered by user
    """
    text_dict = {}
    for char in text:
        if char in text_dict:
            text_dict[char] = text_dict[char] + 1
        else:
            text_dict[char] = 1
    return text_dict

word = input("Enter some word:")
print(calculate_number_of_character(word))



    






