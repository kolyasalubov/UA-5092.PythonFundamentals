def get_num_of_characters(text: str) -> dict[str, int]:
    """Calculates the number of characters included in given string"""
    num_of_chars = {}
    for char in text:
        count = num_of_chars.get(char, 0)
        num_of_chars[char] = count + 1
    return num_of_chars


def main():
    value = input(
        "Enter a text to calculate number of characters included in string: "
    )
    result = get_num_of_characters(value)
    print("Your text includes: ")
    print(result)


if __name__ == '__main__':
    main()
