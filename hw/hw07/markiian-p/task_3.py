def count_characters(text: str) -> dict[str, int]:
    '''calculetes the number of character in given strings'''
    char_count = {}
    for char in text:    
        if char in char_count:
            char_count[char] += 1     
        else:
            char_count[char] = 1
    return char_count
print(count_characters("hello"))