def get_number_of_characters(text):
    output = {}
    
    for char in text:
        if char in output:
            output[char] += 1
        else:
            output[char] = 1
    return output

text = input("Enter a text: ")
print(get_number_of_characters(text))