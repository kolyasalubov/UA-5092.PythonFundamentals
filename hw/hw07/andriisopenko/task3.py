def count_characters(text: str) -> dict:
    result = {}
    for character in text:
        if character in result:
            result[character] += 1
        else:
            result[character] = 1
    return result
print(count_characters("hello"))