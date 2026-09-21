def get_num_of_characters(text: str) -> dict[str, int]: 
    """ Calculates the number of characters included in given string """
    num_of_chars = {}
    for c in text:
        n = num_of_chars.get(c, 0)
        num_of_chars[c] = n + 1
    return num_of_chars


def main():
    value = input("Enter any text to calculate number of characters included in given string: ")
    result = get_num_of_characters(value)
    print("Your text includes: ")
    print(result)


if __name__ == '__main__':
    main()